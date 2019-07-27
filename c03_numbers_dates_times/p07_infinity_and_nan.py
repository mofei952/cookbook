#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/7/27 16:27
# @File    : p07_infinity_and_nan.py
# @Software: PyCharm

# 无穷大与NaN
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c03/p07_infinity_and_nan.html

# 可以使用 float() 来创建它们
a = float('inf')
b = float('-inf')
c = float('nan')
print(a, b, c)

# 使用 math.isinf() 和 math.isnan() 函数测试这些值
import math
print(math.isinf(a))
print(math.isinf(b))
print(math.isnan(c))

# 无穷大数在执行数学计算的时候会传播
print(a + 45)
print(a * 10)
print(10 / a)

# 有些操作是未定义的并会返回一个NaN结果
print(a / a)
print(a + b)

# NaN值会在所有操作中传播，而不会产生异常
print(c + 23)
print(c / 2)
print(c * 2)
print(math.sqrt(c))

# NaN值的一个特别的地方时它们之间的比较操作总是返回False
d = float('nan')
print(c == d)
print(c is d)

# 测试一个NaN值得唯一安全的方法就是使用 math.isnan()
print(math.isnan(c))
