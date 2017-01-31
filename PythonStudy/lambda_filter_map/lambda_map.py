def lambda_map():
    map_me = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    result = map(lambda x: "the letter is %s" % x, map_me)
    print(result)


if __name__ == "__main__":
    lambda_map()
