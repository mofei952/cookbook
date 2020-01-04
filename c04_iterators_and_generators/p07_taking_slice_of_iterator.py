#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/8/11 12:58
# @File    : p07_taking_slice_of_iterator.py
# @Software: PyCharm

"""迭代器切片"""

import itertools


# 定义一个生成器
def count(n):
    while True:
        yield n
        n += 1

# 使用函数 itertools.islice() 在迭代器和生成器上做切片操作
c = count(0)
# print(c[10:20]) # TypeError: 'generator' object is not subscriptable
for x in itertools.islice(count(0), 10, 20):
    print(x)

# 函数 islice() 返回一个可以生成指定元素的迭代器，它通过遍历并丢弃直到切片开始索引位置的所有元素。
# 然后才开始一个个的返回元素，并直到切片结束索引位置。
