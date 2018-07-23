import my_debugger

# debugger = my_debugger.debugger()
# debugger.load("C:\Windows\System32\calc.exe")

debugger = my_debugger.debugger()
pid = raw_input("Enter the PID of the process to attach to:")
debugger.attach(int(pid))
debugger.detach()
import pyd