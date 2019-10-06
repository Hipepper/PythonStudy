from multiprocessing import Process
import time


def func(name):
    time.sleep(2)
    print('hello', name)


if __name__ == '__main__':
    p = Process(target=func, args=('derek',))
    p.start()
    # p.join()
    print('end...')
