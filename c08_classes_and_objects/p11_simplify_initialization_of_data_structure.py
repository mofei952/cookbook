#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2020/5/1 16:04
# @File    : p11_simplify_initialization_of_data_structure.py
# @Software: PyCharm

"""简化数据结构的初始化"""

import math


# 可以在一个基类中写一个公用的 __init__() 函数
class Structure1:
    _fields = []

    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))
        for name, value in zip(self._fields, args):
            setattr(self, name, value)


class Stock(Structure1):
    _fields = ['name', 'shares', 'price']


class Point(Structure1):
    _fields = ['x', 'y']


class Circle(Structure1):
    _fields = ['radius']

    def area(self):
        return math.pi * self.radius ** 2


s = Stock('aa', 10, 30)
p = Point(2, 3)
c = Circle(4.5)
print(s.name, s.shares, s.price)
# s = Stock('1', '2') # TypeError: Expected 3 arguments
print()


class Structure2:
    _fields = []

    def __init__(self, *args, **kwargs):
        if len(args) > len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))

        for name, value in zip(self._fields, args):
            setattr(self, name, value)

        for name in self._fields[len(args):]:
            setattr(self, name, kwargs.pop(name))

        if kwargs:
            raise TypeError('Invalid argument(s): {}'.format(','.join(kwargs)))


class Stock(Structure2):
    _fields = ['name', 'shares', 'price']


s1 = Stock('ACME', 50, 91.1)
s2 = Stock('ACME', 50, price=9.1)
s3 = Stock('ACME', shares=50, price=91.1)
# s4 = Stock('ACME', shares=50)  # KeyError: 'price'
# s5 = Stock('ACME', shares=50, price=91.1, aa=1, bb=2)  # TypeError: Invalid argument(s): aa,bb
print(s1.name, s1.shares, s1.price)
print()


# 也可以将不在 _fields 中的名称加入到属性中去
class Structure3:
    # Class variable that specifies expected fields
    _fields = []

    def __init__(self, *args, **kwargs):
        if len(args) != len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))

        # Set the arguments
        for name, value in zip(self._fields, args):
            setattr(self, name, value)

        # Set the additional arguments (if any)
        extra_args = kwargs.keys() - self._fields
        for name in extra_args:
            setattr(self, name, kwargs.pop(name))

        if kwargs:
            raise TypeError('Duplicate values for {}'.format(','.join(kwargs)))


class Stock(Structure3):
    _fields = ['name', 'shares', 'price']


s1 = Stock('ACME', 50, 91.1)
s2 = Stock('ACME', 50, 91.1, date='8/2/2012')
print(s2.name, s2.shares, s2.price, s2.date)
