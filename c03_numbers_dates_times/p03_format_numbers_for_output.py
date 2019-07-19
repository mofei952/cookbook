#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/7/19 19:48
# @File    : p03_format_numbers_for_output.py
# @Software: PyCharm

# 数字的格式化输出
# 将数字格式化后输出，并控制数字的位数、对齐、千位分隔符和其他的细节。
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c03/p03_format_numbers_for_output.html

# 格式化输出单个数字的时候，可以使用内置的 format() 函数
x = 1234.56789
print(format(x, '0.2f'))
print(format(x, '>10.1f'))
print(format(x, '<10.1f'))
print(format(x, '^10.1f'))
print(format(x, ','))
print(format(x, '0,.1f'))

# 指数记法
print(format(x, 'e'))
print(format(x, '0.2E'))

# 以上格式写法同样适用于字符串的format方法
print('{:>0,.2f}'.format(x))

# 上面演示的技术同时适用于浮点数和 decimal 模块中的 Decimal 数字对象
# 当指定数字的位数后，结果值会根据 round() 函数同样的规则进行四舍五入后返回