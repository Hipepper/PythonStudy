# -*- coding: utf-8 -*-

from ctypes import *
from my_debugger_defines import *

kernel32 = windll.kernel32


class debugger():
    def __init__(self):
        self.h_process = None
        self.pid = None
        self.debugger_active = False
        self.h_thread = None
        self.context = None
        self.exception = None
        self.exception_address = None
        self.breakpoints = {}

    def read_process_memory(self, address, length):
        data = ""
        read_buf = create_string_buffer(length)
        count = c_ulong(0)
        if not kernel32.ReadProcessMemory(self.h_process, address, read_buf, length, byref(count)):
            return False
        else:
            data += read_buf.raw
            return data

    def write_process_memory(self, address, data):
        count = c_ulong(0)
        length = len(data)
        c_data = c_char_p(data[count.value:])
        if not kernel32.WriteProcessMemory(self.h_process, address, c_data, length, byref(count)):
            return False
        else:
            return True

    # 设置断点
    def bp_set(self, address):
        # 看看断点的字典里是不是已经存在这个断点的地址了
        if address not in self.breakpoints.keys():
            try:
                # 先读取原来的一个字节，保存后再写入0xCC
                original_byte = self.read_process_memory(address, 1)
                print(original_byte)
                # print GetLastError()
                res = self.write_process_memory(address, '\xCC')
                if res:
                    print("write success")
                else:
                    print("write fail")
                self.breakpoints[address] = (address, original_byte)
            except:
                return False
        return True

    def func_resolve(self, dll, function):
        handle = kernel32.GetModuleHandleA(dll)
        address = kernel32.GetProcAddress(handle, function)
        kernel32.CloseHandle(handle)
        return address

    def load(self, path_to_exe):
        creation_flags = DEBUG_PROCESS
        startupinfo = STARTUPINFO()
        process_infomation = PROCESS_INFORMATION()
        startupinfo.dwFlags = 0x1
        startupinfo.wShowWindow = 0x1
        startupinfo.cb = sizeof(startupinfo)
        if kernel32.CreateProcessA(path_to_exe,
                                   None,
                                   None,
                                   None,
                                   None,
                                   creation_flags,
                                   None,
                                   None,
                                   byref(startupinfo),
                                   byref(process_infomation)):
            print("[*] We have successfully launched the process!")
            print("[*] PID: %d" % process_infomation.dwProcessId)
            self.h_process = self.open_process(process_infomation.dwProcessId)
        else:
            print("[*] Error: 0x%08x" % kernel32.getLastError())

    def open_process(self, pid):
        h_process = kernel32.OpenProcess(PROCESS_ALL_ACCESS, False, pid)
        return h_process

    def attach(self, pid):
        self.h_process = self.open_process(pid)
        if kernel32.DebugActiveProcess(pid):
            self.debugger_active = True
            self.pid = pid
            # self.run()
        else:
            print("[*] Unable to attach to the process, pid: %d." % int(pid))

    def run(self):
        while self.debugger_active == True:
            self.get_debug_event()

    def get_debug_event(self):
        debug_event = DEBUG_EVENT()
        continue_status = DBG_CONTINUE
        if kernel32.WaitForDebugEvent(byref(debug_event), INFINITE):
            # raw_input("Pressa key to continue...")
            # self.debugger_active = False
            self.h_thread = self.open_thread(debug_event.dwThreadId)
            self.context = self.get_thread_context(debug_event.dwThreadId)
            # print("Event Code: %d, Thread ID: %d" % (debug_event.dwDebugEventCode, debug_event.dwThreadId))
            # 如果是例外事件就，处理它
            if debug_event.dwDebugEventCode == EXCEPTION_DEBUG_EVENT:
                self.exception = debug_event.u.Exception.ExceptionRecord.ExceptionCode
                self.exception_address = debug_event.u.Exception.ExceptionRecord.ExceptionAddress
                # 内存访问异常（如写入一个只读的内存区域）
                if self.exception == EXCEPTION_ACCESS_VIOLATION:
                    pass
                    # print("Access Violation Detected.")
                # 断点
                elif self.exception == EXCEPTION_BREAKPOINT:
                    continue_status = self.exception_handler_breakpoint()
                # 访问了具有PAGE_GUARD属性的保护页面
                elif self.exception == EXCEPTION_GUARD_PAGE:
                    print("Guard Page Access Detected.")
                # 单步
                elif self.exception == EXCEPTION_SINGLE_STEP:
                    print("Single Stepping.")
                    # self.exception_handler_single_step()
            kernel32.ContinueDebugEvent(debug_event.dwProcessId, debug_event.dwThreadId, continue_status)

    def exception_handler_breakpoint(self):
        print("[*]Inside the breakpoint handler.")
        print("ExceptionAddress:0x%08x" % self.exception_address)
        return DBG_CONTINUE

    def detach(self):
        if kernel32.DebugActiveProcessStop(self.pid):
            print("[*] Finish debugging success. Exiting...")
            return True
        else:
            print("[*] Finish debugging failed.")
            return False

    def open_thread(self, tid):
        h_thread = kernel32.OpenThread(THREAD_ALL_ACCESS, None, tid)
        if h_thread is not None:
            return h_thread
        else:
            print("[*] Could not obtain a valid thread handle.")
            return False

    def enumerate_threads(self):
        thread_entry = THREADENTRY32()
        thread_list = []
        snapshot = kernel32.CreateToolhelp32Snapshot(TH32CS_SNAPTHREAD, self.pid)
        if snapshot is not None:
            thread_entry.dwSize = sizeof(thread_entry)
            success = kernel32.Thread32First(snapshot, byref(thread_entry))
            while success:
                if thread_entry.th32OwnerProcessID == self.pid:
                    thread_list.append(thread_entry.th32ThreadID)
                success = kernel32.Thread32Next(snapshot, byref(thread_entry))
            kernel32.CloseHandle(snapshot)
            return thread_list
        else:
            print("[*] enumerate threads fail.")
            return False

    def get_thread_context(self, tid):
        context = CONTEXT()
        context.ContextFlags = CONTEXT_FULL | CONTEXT_DEBUG_REGISTERS
        h_thread = self.open_thread(tid)
        if kernel32.GetThreadContext(h_thread, byref(context)):
            kernel32.CloseHandle(h_thread)
            return context
        else:
            print("[*] get_thread_context fail.")
            return False
