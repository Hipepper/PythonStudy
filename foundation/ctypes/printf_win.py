from ctypes import *

msvcrt = cdll.msvcrt
message = "Hello World!"
msvcrt.printf("%s\n", message)