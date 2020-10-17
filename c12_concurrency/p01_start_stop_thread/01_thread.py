from threading import Thread

from c12_concurrency.p01_start_stop_thread.common import countdown

# 创建一个Thread对象并将要执行的对象以target参数的形式提供给该对象。
t = Thread(target=countdown, args=(3, ))
t.start()

# 查询一个线程对象的状态，看它是否还在执行
if t.is_alive():
    print('Still running')
else:
    print('Completed')

# 可以将一个线程加入到当前线程，并等待它终止
t.join()

if t.is_alive():
    print('Still running')
else:
    print('Completed')

# 主线程直到所有非后台线程都终止前仍保持运行
