from multiprocessing import Process, Pipe


def f(conn):
    conn.send('11')
    conn.send('22')
    print("from parent:", conn.recv())
    print("from parent:", conn.recv())
    conn.close()


if __name__ == '__main__':
    parent_conn, child_conn = Pipe()  # 生成管道实例，可以互相send（）和recv（）

    p = Process(target=f, args=(child_conn,))
    p.start()

    print(parent_conn.recv())  # prints "11"
    print(parent_conn.recv())  # prints "22"
    parent_conn.send("33")  # parent 发消息给 child
    parent_conn.send("44")
    p.join()
