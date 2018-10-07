#!/usr/bin/env python
# -*- coding: utf-8 -*-


def test_first():
    return 3


def test_second(num):
    return num


action = {
    "para": 5,
    "test_first": test_first,
    "test_second": test_second
}


def test_eavl():
    condition = "para == 5 and test_second(test_first()) > 5"
    res = eval(condition, action)
    print(res)


if __name__ == '__main__':
    test_eavl()
