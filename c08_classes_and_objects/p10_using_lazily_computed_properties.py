#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2020/5/1 14:28
# @File    : p10_using_lazily_computed_properties.py
# @Software: PyCharm

"""使用延迟计算属性"""

import math


# 定义一个延迟属性的一种高效方法是通过使用一个描述器类
# 这种方式有一个缺陷是计算出来的值是可以被修改的
class lazyproperty:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            value = self.func(instance)
            setattr(instance, self.func.__name__, value)
            return value


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @lazyproperty
    def area(self):
        print('Computing area')
        return math.pi * self.radius ** 2

    @lazyproperty
    def perimeter(self):
        print('Computing perimater')
        return 2 * math.pi * self.radius


c = Circle(4)
print(vars(c))
print(c.area)
print(vars(c))
print(c.area)
print()


# 让计算后的值不能被修改的方案，和第一个方案比稍微没那么高效
def lazyproperty(func):
    name = '_lazy_' + func.__name__

    @property
    def lazy(self):
        if hasattr(self, name):
            return getattr(self, name)
        else:
            value = func(self)
            setattr(self, name, value)
            return value

    return lazy


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @lazyproperty
    def area(self):
        print('Computing area')
        return math.pi * self.radius ** 2

    @lazyproperty
    def perimeter(self):
        print('Computing perimater')
        return 2 * math.pi * self.radius


c = Circle(4)
# c.area = 1  # AttributeError: can't set attribute
print(c.area)
print()


# 如果一个描述器仅仅只定义了一个 __get__() 方法的话，它比通常的具有更弱的绑定。
# 特别地，只有当被访问属性不在实例底层的字典中时 __get__() 方法才会被触发。
# 如果定义 __set__() 方法则达不到想要的效果
class lazyproperty:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            value = self.func(instance)
            setattr(instance, self.func.__name__, value)
            return value

    def __set__(self, instance, value):
        instance.__dict__[self.func.__name__] = value


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @lazyproperty
    def area(self):
        print('Computing area')
        return math.pi * self.radius ** 2

    @lazyproperty
    def perimeter(self):
        print('Computing perimater')
        return 2 * math.pi * self.radius


c = Circle(4)
print(vars(c))
print(c.area)
print(vars(c))
print(c.area)
