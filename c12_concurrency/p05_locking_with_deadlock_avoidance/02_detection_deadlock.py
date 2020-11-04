import threading
from c12_concurrency.p05_locking_with_deadlock_avoidance.common import acquire


# 如果有多个 acquire() 操作被嵌套调用，
# 可以通过线程本地存储（TLS）来检测潜在的死锁问题。
x_lock = threading.Lock()
y_lock = threading.Lock()


def thread_1():

    while True:
        with acquire(x_lock):
            with acquire(y_lock):
                print('Thread-1')


def thread_2():
    while True:
        with acquire(y_lock):
            with acquire(x_lock):
                print('Thread-2')


t1 = threading.Thread(target=thread_1)
t1.daemon = True
t1.start()

t2 = threading.Thread(target=thread_2)
t2.daemon = True
t2.start()


# 发生崩溃的原因在于，每个线程都记录着自己已经获取到的锁。
# acquire() 函数会检查之前已经获取的锁列表，
# 由于锁是按照升序排列获取的，
# 所以函数会认为之前已获取的锁的id必定小于新申请到的锁，
# 这时就会触发异常。
