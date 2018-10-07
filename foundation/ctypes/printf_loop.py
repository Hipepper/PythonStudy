from ctypes import *
import time

msvcrt = cdll.msvcrt
counter = 0

while True:
    message = "Hello World!"
    msvcrt.printf("%s\n", message)
    msvcrt.printf("Loop iteration %d!\n" % counter)
    time.sleep(2)
    counter += 1
