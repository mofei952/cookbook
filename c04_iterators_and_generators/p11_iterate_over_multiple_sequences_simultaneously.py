#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/8/15 19:26
# @File    : p11_iterate_over_multiple_sequences_simultaneously.py
# @Software: PyCharm

# 同时迭代多个序列
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c04/p11_iterate_over_multiple_sequences_simultaneously.html

# 使用zip函数
xs = [1, 2, 3, 4, 5]
ys = [10, 20, 30, 40, 50]
for x, y in zip(xs, ys):
    print(x, y)

# zip函数的迭代长度跟参数中最短序列长度一致
xs = [1, 2, 3, 4, 5]
ys = [10, 20, 30]
for x, y in zip(xs, ys):
    print(x, y)

# 使用 itertools.zip_longest() 迭代长度和最长序列长度一致，没有值的位置补None
from itertools import zip_longest
for x, y in zip_longest(xs, ys):
    print(x, y)

# 处理表头和数据
headers = ['name', 'shares', 'price']
values = ['ACME', 100, 490.1]
print(dict(zip(headers, values)))

# 处理表头和多行数据
headers = ['name', 'shares', 'price']
data = [['ACME', 100, 490.1], ['CC', 101, 422.1]]
print([dict(zip(headers, line)) for line in data])

# zip 可以接受多于两个序列的参数
xs = [1, 2, 3, 4, 5]
ys = [10, 20, 30, 40, 50]
zs = [100, 200, 300, 400, 500]
for x, y, z in zip(xs, ys, zs):
    print(x, y, z)
