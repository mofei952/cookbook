#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/12/3 20:50
# @File    : p20_perform_text_operations_on_byte_string.py
# @Software: PyCharm

"""字节字符串上的字符串操作"""

import os
import re

# 在字节字符串上执行普通的文本操作
data = b'Hello World'
print(data[0:5])
print(data.startswith(b'Hello'))
print(data.split())
print(data.replace(b'Hello', b'Hello aa'))

# 这些操作同样也适用于字节数组
data = bytearray(b'Hello World')
print(data[0:5])
print(data.startswith(b'Hello'))
print(data.split())
print(data.replace(b'Hello', b'Hello bb'))

# 可以使用正则匹配字节字符串，正则表达式本身必须是字节串
data = b'AAA:BBB,CCC'
print(re.split(b'[:,]', data))

# 和文本字符串不同，字节字符串的索引操作返回整数而不是单独字符
a = 'Hello'
print(a[0])
b = b'Hello'
print(b[0])

# 字节字符串不会提供一个美观的字符串表示，除非先被解码为一个文本字符串
s = b'Hello World'
print(s)
print(s.decode('ascii'))

# 字节字符串不存在格式化操作，要格式化字节字符串要先使用文本字符串再编码为字节字符串
# a = b'%s' % 'aa'  # TypeError: %b requires a bytes-like object, or an object that implements __bytes__, not 'str'
# a = b'{}'.format('aa')  # AttributeError: 'bytes' object has no attribute 'format'
a = '{:10s} {:10d} {:10.2f}'.format('ACME', 100, 490.1).encode('ascii')
print(a)

# 使用字节字符串可能会改变一些操作的语义，特别是那些跟文件系统有关的操作
# 以下os.listdir函数中目录名参数使用字节字符串时会导致文件名以未解码字节返回
with open('p20\xf1o.txt', 'w') as f:
    f.write('spicy')

print(os.listdir('.'))
print(os.listdir(b'.'))
