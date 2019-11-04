#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/10/26 18:14
# @File    : p01_unpack_sequence_into_separate_variables.py
# @Software: PyCharm

"""解压序列赋值给多个变量"""

# 任何的序列（或者是可迭代对象）可以通过一个简单的赋值语句解压并赋值给多个变量
# 唯一的前提就是变量的数量必须跟序列元素的数量是一样的
p = (4, 5)
x, y = p
data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, (year, mon, day) = data

# 如果变量个数和序列元素的个数不匹配，会产生一个异常
p = (4, 5)
# x, y, z = p  # ValueError: not enough values to unpack (expected 3, got 2)

# 这种解压赋值可以用在任何可迭代对象上面，而不仅仅是列表或者元组。 包括字符串，文件对象，迭代器和生成器
s = 'Hello'
a, b, c, d, e = s

# 有时候，只想解压一部分，丢弃其他的值
# 可以使用任意变量名去占位，到时候丢掉这些变量就行了
# 但是保证选用的那些占位变量名在其他地方没被使用到
data = ['ACME', 50, 91.1, (2012, 12, 21)]
_, shares, price, _ = data
