#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/9/17 21:01
# @File    : p14_implementing_custom_containers.py
# @Software: PyCharm

"""实现自定义容器"""

import bisect
import collections


# 尝试实例化一个抽象基类，可以再错误提示中找到需要实现哪些方法
# collections.Sequence()  # TypeError: Can't instantiate abstract class Sequence with abstract methods __getitem__, __len__


# 自定义容器时继承collections.Sequence
class SortedItems(collections.Sequence):
    def __init__(self, initial=None):
        if initial is not None and not isinstance(initial, collections.Sequence):
            raise TypeError('excepted a sequence object')
        self._items = sorted(initial) if initial is not None else []

    def __getitem__(self, index):
        return self._items[index]

    def __len__(self):
        return len(self._items)

    def add(self, item):
        bisect.insort(self._items, item)


# SortedItems和普通序列一样，支持索引、迭代、包含判断、切片等操作
items = SortedItems([5, 1, 4, 3])
print(list(items))
print(items[0])
items.add(2)
print(list(items))
print()

# 使用 collections 中的抽象基类可以确保你自定义的容器实现了所有必要的方法。并且还能简化类型检查。
print(isinstance(items, collections.Iterable))
print(isinstance(items, collections.Sequence))
print(isinstance(items, collections.Container))
print(isinstance(items, collections.Sized))
print(isinstance(items, collections.Mapping))
print()


# collections中很多抽象类会为一些常见容器操作提供默认的实现
# 比如自定义一个继承自collections.MutableSequenece的类
class Items(collections.MutableSequence):
    def __init__(self, initial=None):
        self._items = list(initial) if initial is not None else []

    # Required sequence methods
    def __getitem__(self, index):
        print('Getting:', index)
        return self._items[index]

    def __setitem__(self, index, value):
        print('Setting:', index, value)
        self._items[index] = value

    def __delitem__(self, index):
        print('Deleting:', index)
        del self._items[index]

    def insert(self, index, value):
        print('Inserting:', index, value)
        self._items.insert(index, value)

    def __len__(self):
        print('Len')
        return len(self._items)


# Items的实例支持了几乎所有的核心列表方法
a = Items([1, 2, 3])
print(len(a))
a.append(4)
a.append(2)
print(a.count(2))
a.remove(3)
