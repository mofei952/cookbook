import threading

from c12_concurrency.p05_locking_with_deadlock_avoidance.common import acquire


# 使用死锁避免机制解决“哲学家就餐问题”
def philosopher(left, right):
    while True:
        with acquire(left, right):
            print(threading.currentThread(), 'eating')


NSTICKS = 5
chopsticks = [threading.Lock() for n in range(NSTICKS)]

for n in range(NSTICKS):
    t = threading.Thread(target=philosopher,
                         args=(chopsticks[n], chopsticks[(n+1) % NSTICKS]))
    t.start()
