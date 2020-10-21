import heapq
import threading
from threading import Thread
import random
import time


# 尽管队列是最常见的线程间通信机制，但是仍然可以自己通过创建自己的数据结构并添加所需的锁和同步机制来实现线程间通信。
# 最常见的方法是使用 Condition 变量来包装你的数据结构。
# 下边这个例子演示了如何创建一个线程安全地优先级队列。
class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0
        self._cv = threading.Condition()

    def push(self, item, priority):
        with self._cv:
            heapq.heappush(self._queue, (-priority, self._index, item))
            self._index += 1
            self._cv.notify()

    def pop(self):
        with self._cv:
            while len(self._queue) == 0:
                self._cv.wait()
            return heapq.heappop(self._queue)[-1]

    def qsize(self):
        return len(self._queue)


def producer(out_q):
    while True:
        data = random.randint(1, 100)
        # time.sleep(0.01)

        out_q.push(data, data)

        if data == 100:
            break

    # # Put the sentinel on the queue to indicate completion
    out_q.push(_sentinel, 0)


def consumer(in_q):
    while True:
        data = in_q.pop()

        # Check for termination
        if data is _sentinel:
            in_q.push(_sentinel, 0)
            break

        print(in_q.qsize(), data)


q = PriorityQueue()
_sentinel = object()
t1 = Thread(target=consumer, args=(q,))
t2 = Thread(target=producer, args=(q,))
t1.start()
t2.start()
