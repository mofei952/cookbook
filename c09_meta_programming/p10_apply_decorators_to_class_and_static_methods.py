#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/10/26 17:22
# @File    : p10_apply_decorators_to_class_and_static_methods.py
# @Software: PyCharm

# 为类和静态方法提供装饰器

import time
from functools import wraps
from abc import ABCMeta, abstractmethod


# 要确保 @classmethod 或 @staticmethod 在装饰器链中的第一个位置
def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(end - start)
        return res

    return wrapper


class Spam:
    @timethis
    def instance_method(self, n):
        print(self, n)
        while n > 0:
            n -= 1

    @classmethod
    @timethis
    def class_method(cls, n):
        print(cls, n)
        while n > 0:
            n -= 1

    @staticmethod
    @timethis
    def static_method(n):
        print(n)
        while n > 0:
            n -= 1


s = Spam()
s.instance_method(10000)
Spam.class_method(10000)
Spam.static_method(10000)


# 在抽象基类中定义类方法和静态方法
class A(metaclass=ABCMeta):
    @classmethod
    @abstractmethod
    def class_method(cls):
        pass

    @staticmethod
    @abstractmethod
    def static_method(cls):
        pass
