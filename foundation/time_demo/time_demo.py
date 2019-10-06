import time

print(time.time())
print(time.gmtime())
print(time.localtime())

print(time.mktime(time.localtime()))
print(time.mktime(time.gmtime()))

print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

print(time.asctime(time.localtime()))