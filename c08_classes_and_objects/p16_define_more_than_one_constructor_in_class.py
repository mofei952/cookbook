#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/9/21 16:13
# @File    : p16_define_more_than_one_constructor_in_class.py
# @Software: PyCharm

# 在类中定义多个构造器
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c08/p16_define_more_than_one_constructor_in_class.html

import time


# 为了实现多个构造器，可以使用类方法
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def today(cls):
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)

    def __str__(self):
        return '{:04d}-{:02d}-{:02d}'.format(self.year, self.month, self.day)
        # return "%04d-%02d-%02d" % (self.year, self.month, self.day)


a = Date(2019, 9, 21)
b = Date.today()
print(a)
print(b)


# 类方法接受一个class对象作为第一个参数
# 在继承时也可以很好的工作
class NewDate(Date):
    pass


c = Date.today()  # today(cls=Date)
d = NewDate.today()  # today(cls=NewDate)
print(c)
print(d)
