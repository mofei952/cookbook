#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2020/2/6 16:49
# @File    : p14_bypassing_filename_encoding.py
# @Software: PyCharm

"""忽略文件名编码"""
import os
import sys

# 默认情况，所有文件名都会根据sys.getfilesystemencoding()返回的文本编码来编码或解码
print(sys.getdefaultencoding())

# 如果要忽略这种编码，可以使用一个原始字符串来指定一个文件名即可
with open('p14\xf1o.txt', 'w') as f:
    f.write('aaa')

print([name for name in os.listdir('.') if name.startswith('p14')])
print([name for name in os.listdir(b'.') if name.startswith(b'p14')])

with open(b'p14\xc3\xb1o.txt') as f:
    print(f.read())
