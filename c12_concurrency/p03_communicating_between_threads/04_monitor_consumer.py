from queue import Queue, Empty
from threading import Event, Thread
import random


# 如果一个线程需要在一个“消费者”线程处理完特定的数据项时立即得到通知，
# 你可以把要发送的数据和一个 Event 放到一起使用，
# 这样“生产者”就可以通过这个Event对象来监测处理的过程了。
def producer(out_q):
    while True:
        data = random.randint(1, 100)
        evt = Event()

        out_q.put((data, evt))

        # Wait for the consumer to process the item
        evt.wait()
        print('monitored', data)

        if data > 90:
            break

    out_q.put((_sentinel, None))


def consumer(in_q):
    while True:
        data, evt = in_q.get()

        if data is _sentinel:
            in_q.put((_sentinel, None))
            break

        evt.set()

        print('consumer', data)


q = Queue()
_sentinel = object()
t1 = Thread(target=consumer, args=(q,))
t2 = Thread(target=producer, args=(q,))
t1.start()
t2.start()
