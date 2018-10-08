# -*- coding: utf-8 -*-
class TestGetAttr(object):
    test = "test attribute"

    def say(self):
        print("test method")


def test_getattr():
    my_test = TestGetAttr()
    try:
        print(getattr(my_test, "test"))
    except AttributeError:
        print("Attribute Error!")
    try:
        getattr(my_test, "say")()
    except AttributeError:  # 没有该属性, 且没有指定返回值的情况下
        print("Method Error!")


if __name__ == '__main__':
    test_getattr()
