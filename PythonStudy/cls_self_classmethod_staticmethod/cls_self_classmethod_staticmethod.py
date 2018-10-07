# coding:utf-8
class A:
    member = "this is a test."

    def __init__(self):
        pass

    @classmethod
    def Print1(cls):
        print("print 1: " + cls.member)

    def Print2(self):
        print("print 2: " + self.member)

    @classmethod
    def Print3(paraTest):
        print("print 3: " + paraTest.member)

    @staticmethod
    def print4():
        print("hello")

    a = 'a'

    @staticmethod
    def foo1(name):
        print('hello' + name)
        print(A.a)
        # print(A.foo2('mamq'))

    def foo2(self, name):
        print('hello' + name)

    @classmethod
    def foo3(cls, name):
        print('hello' + name)
        print(A.a)
        print(cls().foo2(name))


a = A()
# A.Print1()
# a.Print1()
# # A.Print2()
# a.Print2()
# A.Print3()
# a.Print3()
# A.print4()

a.foo1('mamq')
A.foo1('mamq')
a.foo2('mamq')
# A.foo2('mamq')
a.foo3('mamq')
A.foo3('mamq')
