from concurrent.futures import ProcessPoolExecutor
import time

# 一个 ProcessPoolExecutor 创建N个独立的Python解释器， N是系统上面可用CPU的个数。
# 你可以通过提供可选参数给 ProcessPoolExecutor(N) 来修改 处理器数量。
# 这个处理池会一直运行到with块中最后一个语句执行完成， 然后处理池被关闭。


def work(x):
    time.sleep(2)
    return x+1


data = [1, 2, 3]


if __name__ == "__main__":
    # # Nonparallel code
    # results = map(work, data)
    # print(list(results))

    # # 使用pool.map来并行执行
    # with ProcessPoolExecutor() as pool:
    #     results = pool.map(work, data)
    #     print(list(results))

    # 使用pool.submit()来手动提交单个任务
    with ProcessPoolExecutor() as pool:
        future_result = pool.submit(work, 1)

        # 如果你手动提交一个任务，结果是一个 Future 实例。
        # 要获取最终结果，你需要调用它的 result() 方法。 它会阻塞进程直到结果被返回来。
        r = future_result.result()
        print(r)
        print('end')

    # 如果不想阻塞，你还可以使用一个回调函数
    def when_done(r):
        print('Got:', r.result())

    with ProcessPoolExecutor() as pool:
        future_result = pool.submit(work, 1)
        future_result.add_done_callback(when_done)
        print('end')
