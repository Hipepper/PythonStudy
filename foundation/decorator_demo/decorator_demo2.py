import time


def timer(func):
    def deco(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        stop_time = time.time()
        print(stop_time - start_time)

    return deco


@timer
def test(parameter):
    time.sleep(1)
    print("test is running")


test("添加参数")
