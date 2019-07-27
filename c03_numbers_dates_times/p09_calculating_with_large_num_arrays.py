#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/7/27 17:40
# @File    : p09_calculating_with_large_num_arrays.py
# @Software: PyCharm

# 大型数组运算
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c03/p09_calculating_with_large_num_arrays.html

# 标准列表对象
x = [1, 2, 3, 4]
y = [5, 6, 7, 8]
print(x * 2)
# print(x + 10) # can only concatenate list (not "int") to list
print(x + y)

# NumPy数组对象
import numpy as np
ax = np.array([1, 2, 3, 4])
ay = np.array([5, 6, 7, 8])
print(ax)
print(ax * 2)
print(ax + 10)
print(ax + ay)
print(ax * ay)

# 计算多项式的值
# 对整个数组中所有元素同时执行数学运算可以使得作用在整个数组上的函数运算简单而又快速
def f(x):
    return 3 * x ** 2 - 2 * x + 7
print(f(ax))

# NumPy 还为数组操作提供了大量的通用函数，这些函数可以作为 math 模块中类似函数的替代
print(np.sqrt(ax))
print(np.cos(ax))

# 使用这些通用函数要比循环数组并使用 math 模块中的函数执行计算要快的多
# 底层实现中， NumPy 数组使用了C或者Fortran语言的机制分配内存。
# 也就是说，它们是一个非常大的连续的并由同类型数据组成的内存区域。
# 所以，你可以构造一个比普通Python列表大的多的数
# 可以很轻松的构造一个10,000*10,000的浮点数二维网格
grid = np.zeros(shape=(10000, 10000), dtype=float)
print(grid)

# 所有的普通操作还是会同时作用在所有元素上
grid += 10
print(grid)
print(np.sin(grid))

# NumPy扩展Python列表的索引功能
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a)
print(a[1])
print(a[:, 1])
print(a[1:3, 1:3])
a[1:3, 1:3] += 10
print(a)
print(a + [100, 101, 102, 103])
print(np.where(a < 10, a, 10))
