import threading, time


class MyThread(threading.Thread):  # 继承threading,Thread模块
    def __init__(self, n):
        super(MyThread, self).__init__()  # 继承父类
        self.n = n

    def run(self):  # 必须用run
        print('task', self.n)
        time.sleep(2)


t1 = MyThread(1)
t2 = MyThread(2)
t1.start()
t2.start()

print('I am main thread')
print(t1.is_alive())  # 返回线程是否活动的。
print(t1.getName())  # 返回线程名。
t1.setName('我是T1')  # 设置线程名。
print(t1.getName())
print(threading.currentThread())  # 查看当前线程是主线程（mainThread）还是子线程(Thread)
print(threading.activeCount())  # 返回正在运行的线程数量
