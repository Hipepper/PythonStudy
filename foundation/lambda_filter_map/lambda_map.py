import sys


def my_map_print(result):
    if sys.version_info.major == 3:
        tmp = []
        for item in result:
            tmp.append(item)
    else:
        tmp = result
    print(tmp)


def lambda_map():
    map_me = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    result = map(lambda x: "the letter is %s" % x, map_me)
    my_map_print(result)


def lambda_map_list():
    map_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result = map(lambda list: [list[1], list[0], list[2]], map_list)
    my_map_print(result)


if __name__ == "__main__":
    lambda_map()
    lambda_map_list()
