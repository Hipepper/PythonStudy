from multiprocessing import Process, Queue  # Queue是进程排列


def f(test):
    test.put('22')  # 通过创建的子进程往队列添加数据，实线父子进程交互


if __name__ == '__main__':
    q = Queue()  # 父进程
    q.put("11")

    p = Process(target=f, args=(q,))  # 子进程
    p.start()
    p.join()

    print("取到：", q.get_nowait())
    print("取到：", q.get_nowait())

    # 父进程在创建子进程的时候就把q克隆一份给子进程
    # 通过pickle序列化、反序列化，来达到两个进程之间的交互
