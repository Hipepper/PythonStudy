import threading
import time


def run(n):  # 定义线程要运行的函数
    print('task', n)
    time.sleep(2)
    print('I am sub thread')


if __name__ == '__main__':
    t1 = threading.Thread(target=run, args=(1,))  # 生成一个线程
    t2 = threading.Thread(target=run, args=(2,))
    t1.start()
    t2.start()

print('I am main thread')  # 主线程
