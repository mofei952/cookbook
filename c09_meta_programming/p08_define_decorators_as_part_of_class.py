#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/10/20 14:50
# @File    : p08_define_decorators_as_part_of_class.py
# @Software: PyCharm

# 将装饰器定义为类的一部分

from functools import wraps


# 在类中定义装饰器
class A:
    def decorator1(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('decorator 1')
            return func(*args, **kwargs)

        return wrapper

    @classmethod
    def decorator2(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('decorator 2')
            return func(*args, **kwargs)

        return wrapper


# 作为一个实例方法被调用
a = A()
@a.decorator1
def spam():
    pass


# 作为一个类方法被调用
@A.decorator2
def grok():
    pass


spam()
grok()


# 要让A中定义的装饰器作用在子类B中，装饰器要被定义成类方法并且必须显式的使用父类名去调用它
# 不能使用 @B.decorator2 ，因为在方法定义时，这个类B还没有被创建
class B(A):
    @A.decorator2
    def bar(self):
        pass
