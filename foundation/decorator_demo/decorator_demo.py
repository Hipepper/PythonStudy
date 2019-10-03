import time


def timer(func):
    def wrapper():
        start_time = time.time()
        func()
        stop_time = time.time()
        print("run time %s" % (stop_time - start_time))
    return wrapper


@timer  # 语法糖  test=timer(test)
def test():
    time.sleep(1)
    print("in the test")


test()
