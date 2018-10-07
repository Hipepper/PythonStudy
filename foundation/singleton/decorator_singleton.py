
def singleton(cls):
    instances = dict()

    def _singleton(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return _singleton


@singleton
class Test(object):
    pass


if __name__ == '__main__':
    t1 = Test()
    t2 = Test()
    print(t1)
    print(t2)
