#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/6/25 18:57
# @File    : p11_naming_slice.py
# @Software: PyCharm

"""
命名切片

代码中如果出现大量的硬编码会使得代码的可读性和可维护性大大降低。
使用 slice() 可以使代码更加清晰可读。
"""

# 从一个记录（比如文件或其他类似格式）中的某些固定位置提取字段
record = '....................100 .......513.25 ..........'
SHARES = slice(20, 23)
PRICE = slice(31, 37)
cost = int(record[SHARES]) * float(record[PRICE])
print(cost)

# 切片对象的用法
items = [0, 1, 2, 3, 4, 5, 6]
a = slice(2, 4)
print(items[a])
items[a] = [10, 11]
print(items)
del items[a]
print(items)

# 获取切片对象的属性
a = slice(5, 50, 2)
print(a.start, a.stop, a.step)

# 可以通过调用切片的 indices(size) 方法将它映射到一个已知大小的序列上。
# 这个方法返回一个三元组 (start, stop, step) ，所有的值都会被缩小，直到适合这个已知序列的边界为止
a = slice(1, 50)
s = 'HelloWorld'
print(a.indices(len(s)))
for i in range(*a.indices(len(s))):
    print(s[i])
