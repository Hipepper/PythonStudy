from urllib import request
import gevent, time
from gevent import monkey

monkey.patch_all()  # 作用：把当前程序的所有的io操作单独做上标记


def f(url):
    print('GET: %s' % url)
    resp = request.urlopen(url)
    data = resp.read()
    print('%d bytes received from %s.' % (len(data), url))


# 同步需要的时间
urls = ['https://www.python.org/',
        'https://www.163.com/',
        'https://www.baidu.com/']
time_start = time.time()
for url in urls:
    f(url)
print("同步cost", time.time() - time_start)

# 下面是异步花费的时间
async_time_start = time.time()
gevent.joinall([
    gevent.spawn(f, 'https://www.python.org/'),
    gevent.spawn(f, 'https://www.163.com/'),
    gevent.spawn(f, 'https://www.baidu.com/'),
])
print("异步cost", time.time() - async_time_start)
