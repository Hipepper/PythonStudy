from greenlet import greenlet


def test1():
    print(12)
    gr2.switch()  # 到这里切换到gr2，执行test2（）
    print(34)
    gr2.switch()  # 切换到上次gr2运行的位置


def test2():
    print(56)
    gr1.switch()  # 切换到上次gr1运行的位置
    print(78)


gr1 = greenlet(test1)  # 启动一个协程gr1
gr2 = greenlet(test2)  # 启动一个协程gr2

gr1.switch()  # 开始运行gr1
