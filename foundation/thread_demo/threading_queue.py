import queue

q = queue.Queue()  # 生成一个队列对象   先入先出
q.put('1')  # put item into the queue
q.put('2')
q.put('3')

print("size: " + str(q.qsize()))  # 看队列大小
print(q.get())  # 从队列中取
print("size: " + str(q.qsize()))

print(q.get(block=True, timeout=None))  # 取不到数据，默认阻塞，timeout设置阻塞时间
print("size: " + str(q.qsize()))
q.get_nowait()  # 如果队列为空，取不到数据，抛出异常，不会阻塞卡主
q = queue.Queue(maxsize=3)  # maxsize可以设置队列的大小，最多允许存三个
w = queue.PriorityQueue  # 优先级
print(q.full())  # 判断队列是否有数据  返回blue值
print(q.empty())  # 判断队列是否是空    返回blue值
