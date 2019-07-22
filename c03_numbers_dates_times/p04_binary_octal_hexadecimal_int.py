#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/7/22 20:05
# @File    : p04_binary_octal_hexadecimal_int.py
# @Software: PyCharm

# 二八十六进制整数
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c03/p04_binary_octal_hexadecimal_int.html

# 使用 bin() , oct() 或 hex() 函数
x = 1234
print(bin(x))
print(oct(x))
print(hex(x))

# 使用 format() 函数可以不输出 0b , 0o 或者 0x 的前缀
print(format(x, 'b'))
print(format(x, 'o'))
print(format(x, 'x'))

# 处理负数时，默认会输出负号
x = -1234
print(format(x, 'b'))
print(format(x, 'x'))

# 要显示32位的无符号值
x = -1234
print(format(2 ** 32 + x, 'b'))
print(format(2 ** 32 + x, 'x'))

# 以不同的进制转换整数字符串，可以使用带有进制的 int() 函数
print(int('4d2', 16))
print(int('10011010010', 2))

# 使用 0x、0b、0o 表示常量
print(0x4d2)
print(0b10011010010)
print(0o2322)