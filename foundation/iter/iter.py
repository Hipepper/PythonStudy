# !/usr/bin/env python
# -*- coding: utf-8 -*-


class TestIter(object):
    def __init__(self):
        self.lst = [1, 2, 3, 4, 5]

    def read(self):
        for ele in range(len(self.lst)):
            yield ele

    def __iter__(self):
        return self.read()

    def __str__(self):
        return ','.join(map(str, self.lst))

    __repr__ = __str__


def test_iter():
    obj = TestIter()
    for num in obj:
        print(num)
    print(obj)


if __name__ == '__main__':
    test_iter()
