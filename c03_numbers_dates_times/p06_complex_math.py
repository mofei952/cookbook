#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/7/25 21:18
# @File    : p06_complex_math.py
# @Software: PyCharm

"""复数的数学运算"""

import math
import cmath

# 使用复数的两种方式
a = complex(2, 4)
print(a)
b = 3 - 5j
print(b)

# 取得对应的实部、虚部和共轭复数
print(a.real)
print(a.imag)
print(a.conjugate())

# 进行常见的数学运算
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(abs(a))

# 进行正弦、余弦或平方根运算
print(cmath.sin(a))
print(cmath.cos(a))
print(cmath.exp(a))

# Python的标准数学函数并不能产生复数值，要使用cmath才可以
# print(math.sqrt(-1))  # ValueError: math domain error
print(cmath.sqrt(-1))
