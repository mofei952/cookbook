from threading import RLock, Thread, current_thread
import time


# RLock （可重入锁）可以被同一个线程多次获取，
# 主要用来实现基于监测对象模式的锁定和同步。
# 在使用这种锁的情况下，当锁被持有时，
# 只有一个线程可以使用完整的函数或者类中的方法。
class SharedCounter:
    _lock = RLock()

    def __init__(self, initial_value=0):
        self._value = initial_value

    def incr(self, delta=1):
        with SharedCounter._lock:
            self._value += delta

    def decr(self, delta=1):
        with SharedCounter._lock:
            if self._value > 0:
                print(current_thread(), self._value)
                self.incr(-delta)
                time.sleep(1)


def worker():
    while counter._value > 0:
        counter.decr()


counter = SharedCounter(10)
t1 = Thread(target=worker)
t2 = Thread(target=worker)
t1.start()
t2.start()
