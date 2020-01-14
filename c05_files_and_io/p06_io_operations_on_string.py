#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/8/25 17:24
# @File    : p06_io_operations_on_string.py
# @Software: PyCharm

"""字符串的I/O操作"""

import io

# 使用 io.StringIO() 类来创建类文件对象操作字符串数据
s = io.StringIO()
s.write('hello\n')
print('world', file=s)
print(repr(s.getvalue()))

s = io.StringIO('Hello\nWorld\n')
print(repr(s.read(4)))
print(repr(s.read()))

# io.StringIO 只能用于文本。如果要操作二进制数据，要使用 io.BytesIO 类来代替
s = io.BytesIO()
s.write(b'bin')
print(s.getvalue())

# 当想要模拟一个普通的文件的时候 StringIO 和 BytesIO 类是很有用的。
# 比如，在单元测试中，可以使用 StringIO 来创建一个包含测试数据的类文件对象， 这个对象可以被传给某个参数为普通文件对象的函数。