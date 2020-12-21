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
