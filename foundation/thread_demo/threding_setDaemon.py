import threading
import time


def run(n):
    print('task', n)
    time.sleep(2)
    print('i am 子线程')  # 主线程结束，setDaemon不管有没有运行完都会被销毁


if __name__ == '__main__':
    t1 = threading.Thread(target=run, args=(1,))
    t2 = threading.Thread(target=run, args=(2,))
    t1.setDaemon(True)  # 设置守护线程,放在start之前
    t1.start()
    t2.setDaemon(True)
    t2.start()

print('I am main thread')
