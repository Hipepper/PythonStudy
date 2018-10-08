#!/usr/bin/env python
# -*- coding: utf-8 -*-
def test_first():
    print("hello")


def test_second():
    test_first()
    print("second")


def test_third():
    print("third")


action = {
    "test_second": test_second,
    "test_third": test_third
}


def test_exec():
    exec("test_second", action)


if __name__ == '__main__':
    test_exec()
