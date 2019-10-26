#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/10/21 20:21
# @File    : p09_define_decorators_as_classes.py
# @Software: PyCharm

# 将装饰器定义为类

import types
from functools import wraps


# 定义一个装饰器来记录函数调用次数
class Profiled:
    def __init__(self, func):
        wraps(func)(self)
        self.ncalls = 0

    def __call__(self, *args, **kwargs):
        self.ncalls += 1
        return self.__wrapped__(*args, **kwargs)

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return types.MethodType(self, instance)


@Profiled
def add(x, y):
    return x + y


class Spam:
    @Profiled
    def bar(self, x):
        print(self, x)


add(2, 3)
add(3, 4)
print(add.ncalls)

s = Spam()
s.bar(1)
s.bar(2)
s.bar(3)
print(Spam.bar.ncalls)


# 这个功能也可以使用闭包和nonlocal变量来实现
def profiled(func):
    ncalls = 0

    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.ncalls += 1
        return func(*args, **kwargs)

    wrapper.ncalls = ncalls
    return wrapper


@profiled
def add(x, y):
    return x + y


add(2, 3)
add(2, 3)
print(add.ncalls)
