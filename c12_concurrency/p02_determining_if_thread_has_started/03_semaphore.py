import threading
import time


# event对象的一个重要特点是当它被设置为真时会唤醒所有等待它的线程。
# 如果你只想唤醒单个线程，最好是使用信号量或者 Condition 对象来替代。考虑一下这段使用信号量实现的代码：
def worker(n, sema):
    print('waiting', n)
    sema.acquire()
    print('Working', n)


sema = threading.Semaphore(0)
nworkers = 10
for n in range(nworkers):
    t = threading.Thread(target=worker, args=(n, sema, ))
    t.start()

for n in range(nworkers):
    time.sleep(2)
    sema.release()
