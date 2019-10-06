from  multiprocessing import Process, Pool
import time
import os


def Foo(i):
    time.sleep(2)
    print("in process", os.getpid())
    return i + 100


def Bar(arg):
    print('-->exec done:', arg, os.getpid())


if __name__ == '__main__':  # 多进程，必须加这一句（windows系统）
    pool = Pool(processes=3)  # 允许进程池同时放入3个进程
    print("主进程", os.getpid())

    for i in range(10):
        pool.apply_async(func=Foo, args=(i,), callback=Bar)  # callback=回调，执行完Foo(),接着执行Bar()
        # pool.apply(func=Foo, args=(i,)) #串行

    print('end')
    pool.close()
    pool.join()  # 进程池中进程执行完毕后再关闭，如果注释，那么程序直接关闭。必须先close(),再join（）
