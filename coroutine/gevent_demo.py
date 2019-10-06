import gevent


def foo():
    print('Running in foo')
    gevent.sleep(2)
    print('阻塞时间最长，最后运行')


def bar():
    print('running in bar')
    gevent.sleep(1)
    print('foo（）还在阻塞，这里第二个运行')


def func3():
    print("running in func3 ")
    gevent.sleep(0)
    print("其它两个还在IO阻塞先运行")


# 创建协程实例
gevent.joinall([
    gevent.spawn(foo),  # 生成，
    gevent.spawn(bar),
    gevent.spawn(func3),
])

# 遇到IO自动切换
