import sys

testabc = 1
print sys.getrefcount(testabc)


class A:
    def __init__(self):
        pass

if __name__ == '__main__':
    a = A()
    print sys.getrefcount(a)