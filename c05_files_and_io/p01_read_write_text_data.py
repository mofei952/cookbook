#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/8/19 20:37
# @File    : p01_read_write_text_data.py
# @Software: PyCharm

# 读写文本数据
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c05/p01_read_write_text_data.html

# 使用带有 rt 模式的 open() 函数读取文本文件
with open('p01.txt', 'rt') as f:
    data = f.read()
    print(data)

# 使用带有wt模式的open函数，会覆盖之前的内容
with open('p01.txt', 'wt') as f:
    f.write('111')
    f.write('222')

# 使用at模式对文件内容进行追加
with open('p01.txt', 'at') as f:
    f.write('333')
    f.write('444')

import sys
print(sys.getdefaultencoding())