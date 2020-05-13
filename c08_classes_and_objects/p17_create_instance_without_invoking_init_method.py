#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/9/21 16:50
# @File    : p17_create_instance_without_invoking_init_method.py
# @Software: PyCharm

"""创建不调用init方法的实例"""

import json
from time import localtime


# 通过__new__方法创建一个未初始化的实例
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day


d = Date.__new__(Date)
print(d)
# print(d.year) # AttributeError: 'Date' object has no attribute 'year'

# 这个Date实例的year属性还不存在，需要手动进行初始化
data = {'year': 2019, 'month': 9, 'day': 21}
for k, v in data.items():
    setattr(d, k, v)
print(d.year)
print(d.month)


# 定义一个today类方法，不使用__init__()初始化对象
class NewDate(Date):
    @classmethod
    def today(cls):
        d = cls.__new__(cls)
        t = localtime()
        d.year = t.tm_year
        d.month = t.tm_mon
        d.day = t.tm_mday
        return d

    def __repr__(self):
        return '{} {:04d}-{:02d}-{:02d}'.format(self.__class__, self.year, self.month, self.day)


print(NewDate.today())


# 反序列化JSON数据时，可以使用__new__函数
class NewNewDate(NewDate):
    @classmethod
    def from_json(cls, data):
        d = cls.__new__(cls)
        d.year = data['year']
        d.month = data['month']
        d.day = data['day']
        return d


print(json.loads('{"year": 2012, "month": 8, "day": 29}', object_hook=NewNewDate.from_json))
