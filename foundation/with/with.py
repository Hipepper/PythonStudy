#!/usr/bin/env python
# -*- coding: utf-8 -*-


class MyWith(object):
    def __init__(self):
        print("__init__ method")

    def __enter__(self):
        print("__enter__ method")
        return self  # 返回对象给as后的变量

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print("__exit__ method")
        if exc_traceback is None:
            print("Exited without Exception")
            return True
        else:
            print("Exited with Exception")
            return False


def test_with():
    with MyWith() as my_with:
        print("running my_with")
    print("------分割线-----")
    with MyWith() as my_with:
        print("running before Exception")
        raise Exception
        print("running after Exception")


if __name__ == '__main__':
    test_with()
