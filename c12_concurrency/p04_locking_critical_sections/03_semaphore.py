from threading import Semaphore, Thread
import urllib.request


# 信号量对象是一个建立在共享计数器基础上的同步原语。
# 如果计数器不为0，with 语句将计数器减1，线程被允许执行。
# with 语句执行结束后，计数器加１。
# 如果计数器为0，线程将被阻塞，直到其他线程结束将计数器加1。
# 比如，你需要限制一段代码的并发访问量，你就可以像下面这样使用信号量完成：
_fetch_url_sema = Semaphore(2)


def fetch_url(url):
    with _fetch_url_sema:
        print('start')
        resp = urllib.request.urlopen(url)
        print(resp.read()[:10])


url = 'http://www.baidu.com'
t1 = Thread(target=fetch_url, args=(url, ))
t2 = Thread(target=fetch_url, args=(url, ))
t3 = Thread(target=fetch_url, args=(url, ))
t1.start()
t2.start()
t3.start()
