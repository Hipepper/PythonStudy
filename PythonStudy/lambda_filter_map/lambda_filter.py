import sys


def my_filter_print(result):
    if sys.version_info.major == 3:
        tmp = []
        for item in result:
            tmp.append(item)
    else:
        tmp = result
    print(tmp)


def lambda_filter():
    filter_me = [1, 2, 3, 4, 6, 7, 8, 11, 12, 14, 15, 19, 22]
    result = filter(lambda x: x % 2 == 0, filter_me)
    my_filter_print(result)


if __name__ == "__main__":
    lambda_filter()
