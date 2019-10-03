from functools import reduce


def f(x, y):
    return x + y


a = reduce(f, [1, 3, 5, 7, 9, 10])
print(a)
