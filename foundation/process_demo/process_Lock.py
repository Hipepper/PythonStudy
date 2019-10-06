from multiprocessing import Process, Lock


def f(l, i):
    l.acquire()
    print('hello world', i)
    l.release()


if __name__ == '__main__':
    lock = Lock()

    for num in range(100):
        Process(target=f, args=(lock, num)).start()  # 要把lock传到函数的参数l

# lock防止在屏幕上打印的时候会乱
