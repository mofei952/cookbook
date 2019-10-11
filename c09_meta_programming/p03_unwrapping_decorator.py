#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/10/4 13:48
# @File    : p03_unwrapping_decorator.py
# @Software: PyCharm

# 解除一个装饰器

import time
from functools import wraps


# 假设装饰器是通过@wraps来实现的，那么可以通过访问__wrapped__属性来访问原始函数
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
def foo():
    print('111')


foo()
origin_foo = foo.__wrapped__
origin_foo()


# 直接访问未包装的原始函数在调试、内省和其他函数操作时是很有用的。
# 但是这个方案仅仅适用于在装饰器中正确使用了@wraps或者直接设置了__wrapped__属性的情况


# 如果有多个装饰器，那么访问__wrapped__属性的行为是不可预知的，应该避免这样做。
# 在python3.3中，它会略过所有的包装层，3.3以上版本则只会略过最外层。
# 以下代码需要在以上两种版本种运行才能看出区别。
def decorator1(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Decorator 1')
        return func(*args, **kwargs)

    return wrapper


def decorator2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Decorator 2')
        return func(*args, **kwargs)

    return wrapper


@decorator1
@decorator2
def add(x, y):
    return x + y


print(add(2, 3))
print(add.__wrapped__(2, 3))
