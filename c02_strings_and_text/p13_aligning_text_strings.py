#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/7/11 21:08
# @File    : p13_aligning_text_strings.py
# @Software: PyCharm

"""字符串对齐"""

# 基本的字符串对齐操作，可以使用字符串的 ljust() , rjust() 和 center() 方法
text = 'Hello World'
print(text.ljust(20))
print(text.rjust(20))
print(text.center(20))

# 以上方法都能接受一个可选的填充字符
print(text.rjust(20, '='))
print(text.center(20, '*'))

# 函数 format() 同样可以用来很容易的对齐字符串
print(format(text, '>20'))
print(format(text, '<20'))
print(format(text, '^20'))
print(format(text, '=>20s'))
print(format(text, '*^20s'))

# 当格式化多个值的时候，这些格式代码也可以被用在 format() 方法中
print('{:>10s} {:>10s}'.format('Hello', 'World'))

# format() 函数的一个好处是它不仅适用于字符串。它可以用来格式化任何值，使得它非常的通用。
x = 1.2345
print(format(x, '>10'))
print(format(x, '^10.2f'))

# 应该优先选择 format() 函数或者方法。
# format() 要比 % 操作符的功能更为强大。
# 并且 format() 也比使用 ljust() , rjust() 或 center() 方法更通用，
# 因为它可以用来格式化任意对象，而不仅仅是字符串。
