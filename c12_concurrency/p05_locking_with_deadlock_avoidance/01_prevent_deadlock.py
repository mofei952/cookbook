import threading
from c12_concurrency.p05_locking_with_deadlock_avoidance.common import acquire


# 使用 acquire() 函数来申请锁
x_lock = threading.Lock()
y_lock = threading.Lock()


def thread_1():
    while True:
        with acquire(x_lock, y_lock):
            print('Thread-1')


def thread_2():
    while True:
        with acquire(y_lock, x_lock):
            print('Thread-2')


t1 = threading.Thread(target=thread_1)
t2 = threading.Thread(target=thread_2)
t1.start()
t2.start()


# 即使在不同的函数中以不同的顺序获取锁也不会发生死锁
# 其关键在于，在acquire函数中，我们对这些锁进行了排序。
# 通过排序，使得不管用户以什么样的顺序来请求锁，
# 这些锁都会按照固定的顺序被获取。
