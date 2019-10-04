#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/10/4 10:43
# @File    : p01_put_wrapper_around_function.py
# @Software: PyCharm

# 在函数上添加包装器
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c09/p01_put_wrapper_around_function.html

import time
from functools import wraps


# 一个装饰器就是一个函数，它接受一个函数作为参数并返回一个新的函数
def timethis(func):
    """Decorator that reports the execute time"""

    @wraps(func)  # wraps会保留原始函数得元数据
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return result

    return wrapper


@timethis
def countdown(n):
    while n > 0:
        n -= 1


# @timethis和以下语句效果相同
# countdown = timethis(countdown)

countdown(10000)
countdown(100000)
countdown(1000000)

# 内置装饰器有@staticmethod, @classmethod, @property
