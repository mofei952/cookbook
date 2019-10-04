#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/10/4 11:07
# @File    : p02_preserve_function_metadata_when_write_decorators.py
# @Software: PyCharm

# 创建装饰器时保留函数元信息
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c09/p02_preserve_function_metadata_when_write_decorators.html

import time
from functools import wraps
from inspect import signature


# 不加@wraps 被装饰得函数会丢失有用的信息
def timethis(func):
    '''
    Decorator that reports the execution time.
    '''

    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return result

    return wrapper


@timethis
def countdown(n):
    '''
    Counts down
    '''
    while n > 0:
        n -= 1


countdown(100000)
print(countdown.__name__)
print(countdown.__doc__)


# 使用functools库中的@wraps装饰器来注解底层包装函数
def timethis(func):
    '''
    Decorator that reports the execution time.
    '''

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return result

    return wrapper


@timethis
def countdown(n):
    '''
    Counts down
    '''
    while n > 0:
        n -= 1


countdown(100000)
print(countdown.__name__)
print(countdown.__doc__)

# @warps有一个重要特性 是可以通过属性__wrapped__访问被包装函数
countdown.__wrapped__(100000)

# __wrapped__属性还能让被装饰函数正确暴露底层的参数签名信息
print(signature(countdown))
