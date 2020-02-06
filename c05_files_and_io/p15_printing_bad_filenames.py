#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2020/2/6 17:20
# @File    : p15_printing_bad_filenames.py
# @Software: PyCharm

"""打印不合法的文件名"""
import os

# 假定有一个没有正确编码的文件名
import sys

files = os.listdir('.')
files = ['spam.py', 'b\udce4d.txt', 'foo.txt']


# 当不合规范的文件名要输出到屏幕或日志文件时，会抛出编码异常
# for name in files:
#     print(name) # UnicodeEncodeError: 'utf-8' codec can't encode character '\udce4' in position 1: surrogates not allowed

# 碰到不合法文件名时采取补救措施
def bad_filename(filename):
    return repr(filename)[1:-1]


for name in files:
    try:
        print(name)
    except UnicodeEncodeError:
        print(bad_filename(name))
print()


# 另一种补救方式是通过某种方式重新编码
def bad_filename(filename):
    temp = filename.encode(sys.getfilesystemencoding(), errors='surrogateescape')
    return temp.decode('latin-1')


for name in files:
    try:
        print(name)
    except UnicodeEncodeError:
        print(bad_filename(name))
