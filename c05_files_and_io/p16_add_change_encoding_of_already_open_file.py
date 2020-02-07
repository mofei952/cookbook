#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2020/2/6 17:52
# @File    : p16_add_change_encoding_of_already_open_file.py
# @Software: PyCharm

"""增加或改变已打开文件的编码"""

import sys
import urllib.request
import io

# 给一个以二进制模式打开的文件添加unicode编码/解码方式，可以使用io.TextIOWrapper()对象包装它
# u = urllib.request.urlopen('http://www.baidu.com')
u = open('p16.txt', 'rb')
f = io.TextIOWrapper(u, encoding='utf-8')
text = f.read()
print(text)
print(type(text))
u.close()

# 如果想修改一个已经打开的文件模式的文件的编码方式，可以先使用detach()方法移除调已存在的文本编码层，并使用新的编码方式代替
u = open('p16.txt', encoding='utf8')
print(u.encoding)
print(u.read())
u = io.TextIOWrapper(u.detach(), encoding='latin-1')
print(u.encoding)
u.seek(0)
print(u.read())

# I/O系统由一系列的层次构建而成
f = open('p16.txt', 'w')
print(f)  # io.TextIOWrapper是一个编码和解码unicode的文本处理层
print(f.buffer)  # io.BufferedWriter是一个处理二进制数据的带缓冲的I/O层
print(f.buffer.raw)  # io.FileIO是一个表示操作系统底层文件描述符的原始文件

# 这种技术还可以用来改变文件行处理、错误机制以及文件处理的其他方面
# sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='ascii', errors='xmlcharrefreplace')
print('Jalape\u00f1o'.encode())
