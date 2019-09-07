#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/9/6 21:04
# @File    : p04_save_memory_when_create_large_number_instances.py
# @Software: PyCharm

# 创建大量对象时节省内存方法
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c08/p04_save_memory_when_create_large_number_instances.html

# 对于主要是用来当成简单的数据结构的类而言，
# 可以通过给类添加 __slots__ 属性来极大的减少实例所占的内存
# 使用slots后不再为每个实例定义一个字典存储实例的属性，从而节省内存
class Date:
    __slots__ = ['year', 'month', 'day']

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

# 关于 __slots__ 的一个常见误区是它可以作为一个封装工具来防止用户给实例增加新的属性。
# 尽管使用slots可以达到这样的目的，但是这个并不是它的初衷。
# __slots__ 更多的是用来作为一个内存优化工具。
