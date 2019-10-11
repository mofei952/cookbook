#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/10/4 10:43
# @File    : p01_put_wrapper_around_function.py
# @Software: PyCharm

# 在函数上添加包装器

import time
from functools import wraps


# 如果想要使用额外的代码包装一个函数，可以定义一个装饰器函数
def timethis(func):
    """Decorator that reports the execute time"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return result

    return wrapper


# 使用装饰器
@timethis
def countdown(n):
    while n > 0:
        n -= 1


countdown(10000)
countdown(100000)
countdown(1000000)


# 一个装饰器就是一个函数，它接受一个函数作为参数并返回一个新的函数。

# @timethis和以下写法是等价的
def countdown(n):
    while n > 0:
        n -= 1


countdown = timethis(countdown)

countdown(10000)
countdown(100000)
countdown(1000000)

# 内置装饰器有@staticmethod, @classmethod, @property。

# 装饰器内部定义了一个使用*args和**kwargs来接受任意参数的函数。
# 在这个函数里面调用了原始函数并将其结果返回，还可以在这个函数中添加其他额外的代码（比如计时）。
# 然后装饰器会返回这个函数来代替原始函数。

# @wraps(func)注解是很重要的，它能保留原始函数的元数据。
