
import time
import multiprocessing


# 上文所写的那些代码、函数都是与 threading 库无关的，
# 这样就使得这些代码可以被用在其他的上下文中，可能与线程有关，也可能与线程无关。
# 比如，你可以通过 multiprocessing 模块在一个单独的进程中执行你的代码：
class CountdownTask():
    def __init__(self, n):
        super().__init__()
        self.n = n

    def run(self):
        while self.n > 0:
            print('T-minus', self.n)
            self.n -= 1
            time.sleep(1)


if __name__ == "__main__":
    c = CountdownTask(5)
    p = multiprocessing.Process(target=c.run)
    p.start()
