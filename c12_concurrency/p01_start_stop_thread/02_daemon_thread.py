from threading import Thread

from c12_concurrency.p01_start_stop_thread.common import countdown

# 对于需要长时间运行的线程或者需要一直运行的后台任务，应当考虑使用后台线程。
# 后台线程会在主线程终止时自动销毁。
t = Thread(target=countdown, args=(10,), daemon=True)
t.start()

t.join()
