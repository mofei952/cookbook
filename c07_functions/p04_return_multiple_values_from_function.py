#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/8/27 22:12
# @File    : p04_return_multiple_values_from_function.py
# @Software: PyCharm

# 返回多个值的函数
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c07/p04_return_multiple_values_from_function.html

# 函数可以return一个元组，括号可以省略，实际上还是先创建了一个元组然后返回的
def myfun():
    return 1, 2, 3


a, b, c = myfun()
print(a, b, c)

# 返回结果可以赋给多个变量，其实就是元组解包，
# 也可以赋给一个变量，这时候这个变量就是元组本身
x = myfun()
print(x)
