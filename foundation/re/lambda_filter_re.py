import sys
import re


def my_filter_print(result):
    if sys.version_info.major == 3:
        tmp = []
        for item in result:
            tmp.append(item)
    else:
        tmp = result
    print(tmp)


def lambda_filter_re():
    s = ('xxx', 'abcxxxabc', 'xyx', 'abc', 'x.x', 'axa', 'axxxxa', 'axxya')
    result = filter(lambda x: re.match(r'xxx', x), s)
    my_filter_print(result)
    result = filter(lambda x: re.search(r'xxx', x), s)
    my_filter_print(result)
    result = filter(lambda x: re.search(r'x.x', x), s)
    my_filter_print(result)
    result = filter(lambda x: re.search(r'x\.x', x), s)
    my_filter_print(result)
    result = filter(lambda x: re.search(r'x.*x', x), s)
    my_filter_print(result)
    result = filter(lambda x: re.search(r'x.+x', x), s)
    my_filter_print(result)
    result = filter(lambda x: re.search(r'c+', x), s)
    my_filter_print(result)
    result = filter(lambda x: re.search(r'^[^c]*$', x), s)
    my_filter_print(result)


if __name__ == "__main__":
    lambda_filter_re()
