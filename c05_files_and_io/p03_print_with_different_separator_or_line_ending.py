#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/8/20 21:44
# @File    : p03_print_with_different_separator_or_line_ending.py
# @Software: PyCharm

# 使用其他分隔符或行终止符打印
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c05/p03_print_with_different_separator_or_line_ending.html

# 使用print()函数时，改变默认的分隔符或者行尾符
print('aa', 1, 22)
print('aa', 1, 22, sep=',')
print('aa', 1, 22, sep=',', end='!!!\n')

# 使用end参数禁止换行
for i in range(5):
    print(i, end=' ')
print()

# 使用*号表达式输出迭代器的所有元素
row = ('aa', 1, 22)
print(*row, sep=',')
