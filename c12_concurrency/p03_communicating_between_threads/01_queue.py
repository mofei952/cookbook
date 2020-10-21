import time
from queue import Queue
from threading import Thread
import random


# 从一个线程向另一个线程发送数据最安全的方式可能就是使用 queue 库中的队列了。
# Queue 对象已经包含了必要的锁，所以你可以通过它在多个线程间多安全地共享数据。
# 创建一个被多个线程共享的 Queue 对象，这些线程通过使用 put() 和 get() 操作来向队列中添加或者删除元素。
def producer(out_q):
    while True:
        data = random.randint(1, 100)
        time.sleep(1)

        out_q.put(data)

        if data > 90:
            break

    # # Put the sentinel on the queue to indicate completion
    out_q.put(_sentinel)


def consumer(in_q):
    while True:
        data = in_q.get()

        # Check for termination
        if data is _sentinel:
            in_q.put(_sentinel)
            break

        print(in_q.qsize(), data)


q = Queue()
_sentinel = object()
t1 = Thread(target=consumer, args=(q,))
t2 = Thread(target=producer, args=(q,))
t1.start()
t2.start()
