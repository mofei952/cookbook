#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/10/26 17:22
# @File    : p18_map_names_to_sequence_elements.py
# @Software: PyCharm

# 映射名称到序列元素
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c01/p18_map_names_to_sequence_elements.html

# 通过下标访问列表或者元组中元素的代码，但是这样有时候会使得代码难以阅读，那么通过名称来访问元素。
# 使用nametuple, namedtuple会返回一个元组的子类
from collections import namedtuple

Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')
print(sub)  # Subscriber(addr='jonesy@example.com', joined='2012-10-19')
print(sub[0])  # jonesy@example.com
print(sub.addr)  # jo   nesy@example.com
print(sub.joined)  # 2012-10-19

# 尽管 namedtuple 的实例看起来像一个普通的类实例，但是它跟元组类型是可交换的，支持所有的普通元组操作，比如索引和解压
print(len(sub))
addr, joined = sub
print(addr, joined)


# 使用普通元组的代码
def compute_cost(records):
    total = 0.0
    for rec in records:
        total += rec[1] * rec[2]
    return total


# 下标操作通常会让代码表意不清晰，并且非常依赖记录的结构，下面是使用命名元组的版本
Stock = namedtuple('Stock', ['name', 'shares', 'price'])
def compute_cost2(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total


# 命名元组不可更改
s = Stock('ACME', 100, 123.45)
# s.shares = 75  # AttributeError: can't set attribute


# 如果需要改变属性的值，那么可以使用命名元组实例的 _replace() 方法，
# 它会创建一个全新的命名元组并将对应的字段用新的值取代
s = s._replace(shares=75)
print(s)  # Stock(name='ACME', shares=75, price=123.45)

# 可以先创建一个包含缺省值的原型元组，然后使用 _replace() 方法创建新的值被更新过的实例
Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])
stock_prototype = Stock('', 0, 0.0, None, None)
def dict_to_stock(s):
    return stock_prototype._replace(**s)
a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
print(dict_to_stock(a))  # Stock(name='ACME', shares=100, price=123.45, date=None, time=None)
b = {'name': 'ACME', 'shares': 100, 'price': 123.45, 'date': '12/17/2012'}
print(dict_to_stock(b))  # Stock(name='ACME', shares=100, price=123.45, date='12/17/2012', time=None)
