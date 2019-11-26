#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/7/27 16:50
# @File    : p08_calculating_with_fractions.py
# @Software: PyCharm

"""分数运算"""

from fractions import Fraction

# fractions 模块可以被用来执行包含分数的数学运算
a = Fraction(5, 4)
b = Fraction(7, 16)
print(a + b)
print(a * b)

# 获取分子和分母
c =  a * b
print(c.numerator)
print(c.denominator)

# 转为float
print(float(c))

# 限制分母后的值
print(c.limit_denominator(8))

# float转为分数
x = 3.75
y = Fraction(*x.as_integer_ratio())
print(y)