#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/9/2 19:08
# @File    : p10_carry_extra_state_with_callback_functions.py
# @Software: PyCharm

"""
带额外状态信息的回调函数

代码中需要依赖到回调函数的使用(比如事件处理器、等待后台任务完成后的回调等)， 并且还需要让回调函数拥有额外的状态值，以便在它的内部使用到。
"""


# 使用回调函数
def apply_async(func, args, *, callback):
    # Compute the result
    result = func(*args)

    # Invoke the callback with the result
    callback(result)


def print_result(result):
    print('Got:', result)


def add(x, y):
    return x + y


apply_async(add, (2, 3), callback=print_result)
apply_async(add, ('hello', 'world'), callback=print_result)


# 为了让回调函数访问外部信息，一种方法是使用一个绑定方法来代替一个简单函数
class ResultHandler:

    def __init__(self):
        self.sequence = 0

    def handler(self, result):
        self.sequence += 1
        print('[{}] Got: {}'.format(self.sequence, result))


r = ResultHandler()
apply_async(add, (2, 3), callback=r.handler)
apply_async(add, ('hello', 'world'), callback=r.handler)


# 作为类的替代，使用一个闭包捕获状态值
def make_handler():
    sequence = 0

    def handler(result):
        nonlocal sequence
        sequence += 1
        print('[{}] Got: {}'.format(sequence, result))

    return handler


handler = make_handler()
apply_async(add, (2, 3), callback=handler)
apply_async(add, ('hello', 'world'), callback=handler)


# 使用协程实现
def make_handler():
    sequence = 0
    while True:
        result = yield
        sequence += 1
        print('[{}] Got: {}'.format(sequence, result))


handler = make_handler()
next(handler)
apply_async(add, (2, 3), callback=handler.send)
apply_async(add, ('hello', 'world'), callback=handler.send)
