#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/9/3 19:41
# @File    : p11_inline_callback_functions.py
# @Software: PyCharm

"""内联回调函数"""

from queue import Queue
from functools import wraps


# 编写使用回调函数的代码的时候，很多小函数的扩张可能会弄乱程序控制流。
# 希望找到某个方法来让代码看上去更像是一个普通的执行序列，通过使用生成器和协程可以使得回调函数内联在某个函数中
def apply_async(func, args, *, callback):
    # Compute the result
    result = func(*args)

    # Invoke the callback with the result
    callback(result)


class Async:
    def __init__(self, func, args):
        self.func = func
        self.args = args


def inlined_async(func):
    @wraps(func)
    def wrapper(*args):
        f = func(*args)
        result_queue = Queue()
        result_queue.put(None)
        while True:
            result = result_queue.get()
            try:
                a = f.send(result)
                apply_async(a.func, a.args, callback=result_queue.put)
            except StopIteration:
                break

    return wrapper


def add(x, y):
    return x + y


@inlined_async
def test():
    r = yield Async(add, (2, 3))
    print(r)
    r = yield Async(add, ('hello', 'world'))
    print(r)
    for n in range(10):
        r = yield Async(add, (n, n))
        print(r)
    print('Goodbye')


if __name__ == '__main__':
    import multiprocessing

    pool = multiprocessing.Pool()
    apply_async = pool.apply_async

    test()
