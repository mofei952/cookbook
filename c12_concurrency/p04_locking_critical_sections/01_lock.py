from threading import Thread, Lock, current_thread
import time


# 要在多线程程序中安全使用可变对象，你需要使用 threading 库中的 Lock 对象，
# 就像下边这个例子这样：
class SharedCounter:
    def __init__(self, initial_value=0):
        self._value = initial_value
        self._value_lock = Lock()

    def incr(self, delta=1):
        with self._value_lock:
            self._value += delta
            print(self._value)

    def decr(self, delta=1):
        with self._value_lock:
            if self._value > 0:
                print(current_thread(), self._value)
                self._value -= delta
                time.sleep(1)


def worker():
    while counter._value > 0:
        counter.decr()


counter = SharedCounter(10)
t1 = Thread(target=worker)
t2 = Thread(target=worker)
t1.start()
t2.start()
