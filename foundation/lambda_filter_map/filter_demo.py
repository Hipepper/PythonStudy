def is_odd(x):
    return x % 2 == 1


a = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8])
print(list(a))
