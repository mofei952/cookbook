from queue import Queue, Empty
from threading import Event, Thread
import random
import time


# 使用队列来进行线程间通信是一个单向、不确定的过程。
# 通常情况下，你没有办法知道接收数据的线程是什么时候接收到的数据并开始工作的。
# 不过队列对象提供一些基本完成的特性，比如下边这个例子中的 task_done() 和 join() ：
def producer(out_q):
    while running:
        data = random.randint(1, 100)

        out_q.put(data)

        if data > 90:
            break


def consumer(in_q):
    while running:
        try:
            data = in_q.get(timeout=5)
        except Empty:
            continue

        print(data)

        in_q.task_done()


q = Queue()
running = True
t1 = Thread(target=consumer, args=(q,))
t2 = Thread(target=producer, args=(q,))
t1.start()
t2.start()

# Wait for all produced items to be consumed
q.join()

running = False
