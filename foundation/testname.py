# coding:utf-8
print(__name__)

import os

for n in os.listdir('.'):
    print n, os.stat(n).st_size

print "测试"

import sys

a = "嘿嘿嘿"
a = 1
print sys.getrefcount("test")


module = __import__("test_class")
print module

application = getattr(module, "app")
application.test()

