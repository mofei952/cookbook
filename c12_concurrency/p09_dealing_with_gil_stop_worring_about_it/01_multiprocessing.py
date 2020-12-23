from time import sleep


# 如果完全工作于Python环境中，
# 你可以使用 multiprocessing 模块来创建一个进程池，
# 并像协同处理器一样的使用它。
pool = None


# Performs a large calculation (CPU bound)
def some_work(n):
    count = 0
    for i in range(n):
        count += i
    return count


# A thread that calls the above function
def some_thread():
    while True:
        r = pool.apply(some_work, (10, ))
        print(r)
        sleep(2)


# Initiaze the pool
if __name__ == '__main__':
    import multiprocessing
    pool = multiprocessing.Pool()

    some_thread()


# 当一个线程想要执行CPU密集型工作时，会将任务发给进程池。
# 然后进程池会在另外一个进程中启动一个单独的Python解释器来工作。
# 当线程等待结果的时候会释放GIL。
