from threading import Event

from c12_concurrency.p10_defining_an_actor_task.s01_actor_mode_using_thread import \
    Actor


# 可以以元组形式传递标签消息，让actor执行不同的操作
class TaggedActor(Actor):
    def run(self):
        while True:
            tag, *payload = self.recv()
            getattr(self, 'do_'+tag)(*payload)

    def do_A(self, x):
        print('Running A', x)

    def do_B(self, x, y):
        print('Running B', x, y)


a = TaggedActor()
a.start()
a.send(('A', 1))      # Invokes do_A(1)
a.send(('B', 2, 3))   # Invokes do_B(2,3)
a.close()
a.join()


# 下面的actor允许在一个工作者中运行任意的函数，
# 并且通过一个特殊的Result对象返回结果
class Result:
    def __init__(self):
        self._evt = Event()
        self._result = None

    def set_result(self, value):
        self._result = value
        self._evt.set()

    def result(self):
        self._evt.wait()
        return self._result


class Worker(Actor):
    def submit(self, func, *args, **kwargs):
        r = Result()
        self.send((func, args, kwargs, r))
        return r

    def run(self):
        while True:
            func, args, kwargs, r = self.recv()
            r.set_result(func(*args, **kwargs))


worker = Worker()
worker.start()
r = worker.submit(pow, 2, 3)
worker.close()
worker.join()
print(r.result())
