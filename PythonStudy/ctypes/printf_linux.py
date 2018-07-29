from ctypes import *

msvcrt = CDLL("libc.so.6")
message = "Hello World!"
msvcrt.printf("%s\n", message)