#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/9/7 19:08
# @File    : p06_create_managed_attributes.py
# @Software: PyCharm

"""创建可管理的属性"""

import math


# 定义某个属性的一种简单方法是将它定义为一个property
class Person:
    def __init__(self, first_name):
        self.first_name = first_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value

    @first_name.deleter
    def first_name(self):
        raise AttributeError("Can't delete a attribute")


p = Person('aaa')
print(p.first_name)
# p.first_name = 1  # TypeError: Expected a string
p.first_name = 'bbb'
print(p.first_name)


# 也可以在已存在的get和set方法基础上定义property
class Person:
    def __init__(self, first_name):
        self.first_name = first_name

    def get_first_name(self):
        return self._first_name

    def set_first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Excepted a string')
        self._first_name = value

    def del_first_name(self):
        raise AttributeError("Can't delete attribute")

    first_name = property(get_first_name, set_first_name, del_first_name)


p = Person('aaa')
print(p.first_name)
# p.first_name = 1  # TypeError: Expected a string
p.first_name = 'bbb'
print(p.first_name)


# property是一种定义动态计算attribute的方法。
# 这种类型的attributes并不会被实际的存储，而是在需要的时候计算出来。
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @property
    def diameter(self):
        return self.radius * 2

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius


c = Circle(4)
print(c.radius)
print(c.area)
print(c.perimeter)
