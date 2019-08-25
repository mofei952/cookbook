#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/8/25 17:24
# @File    : p06_io_operations_on_string.py
# @Software: PyCharm

# 字符串的I/O操作
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c05/p06_io_operations_on_string.html

import io

# 使用操作类文件对象的程序来操作文本或二进制字符串
s = io.StringIO()
s.write('hello ')
print('world', file=s)
print(s.getvalue())

s = io.BytesIO()
s.write(b'bin')
print(s.getvalue())

# 当想要模拟一个普通的文件的时候 StringIO 和 BytesIO 类是很有用的。
# 比如，在单元测试中，可以使用 StringIO 来创建一个包含测试数据的类文件对象，
# 这个对象可以被传给某个参数为普通文件对象的函数。
#
# 需要注意的是， StringIO 和 BytesIO 实例并没有正确的整数类型的文件描述符。
# 因此，它们不能在那些需要使用真实的系统级文件如文件，管道或者是套接字的程序中使用。
