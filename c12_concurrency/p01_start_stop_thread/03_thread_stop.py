import time
from threading import Thread


# 如果需要终止线程，那么这个线程必须通过编程在某个特定点轮询来退出。
class CountdownTask:
    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False

    def run(self, n):
        while self._running and n > 0:
            print('T-minus', n)
            n -= 1
            time.sleep(1)


c = CountdownTask()
t = Thread(target=c.run, args=(10,))
t.start()

time.sleep(2)
c.terminate()
