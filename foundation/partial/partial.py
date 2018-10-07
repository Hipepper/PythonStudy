from functools import partial


# def partial(func, *part_args):
#     def wrapper(*extra_args):
#         args = list(part_args)
#         args.extend(extra_args)
#         return func(*args)
#     return wrapper


def sum(a, b):
    return a + b


def test_partial():
    fun = partial(sum, 2)
    print(fun(3))


if __name__ == '__main__':
    test_partial()
