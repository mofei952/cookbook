#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/7/17 21:24
# @File    : p01_round_number.py
# @Software: PyCharm

"""数字的四舍五入"""

# 使用内置的 round(value, ndigits) 函数
print(round(1.23, 1))
print(round(1.27, 1))
print(round(-1.27, 1))
print(round(1.25361, 3))

# 当一个值刚好在两个边界的中间的时候， round 函数返回离它最近的偶数。
# 也就是说，对1.5或者2.5的舍入运算都会得到2。
print(round(1.5))
print(round(2.5))

# 传给 round() 函数的 ndigits 参数可以是负数，这种情况下， 舍入运算会作用在十位、百位、千位等上面
a = 1627731
print(round(a, -1))
print(round(a, -2))
print(round(a, -3))

# 在格式化的时候指定精度
x = 1.23456
print(format(x, '0.2f'))
print(format(x, '0.3f'))
print('value is {:0.3f}'.format(x))

# 不要试着去舍入浮点值来”修正”表面上看起来正确的问题
# 对于大多数使用到浮点的程序，没有必要也不推荐这样做。
# 尽管在计算的时候会有一点点小的误差，但是这些小的误差是能被理解与容忍的。
# 如果不能允许这样的小误差(比如涉及到金融领域)，那么就得考虑使用 decimal 模块了
a = 2.1
b = 4.2
c = a + b
print(c)
c = round(c, 2)  # "Fix" result (???) 不推荐
print(c)
