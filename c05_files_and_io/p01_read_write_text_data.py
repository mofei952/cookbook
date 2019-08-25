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
    f.write('444\n')

# 在Unix和Windows中是不一样的(分别是 \n 和 \r\n )。
# 默认情况下，Python会以统一模式处理换行符。
# 这种模式下，在读取文本的时候，Python可以识别所有的普通换行符并将其转换为单个 \n 字符。
# 类似的，在输出时会将换行符 \n 转换为系统默认的换行符。
# 如果不希望这种默认的处理方式，可以给 open() 函数传入参数 newline='' 。
with open('p01.txt', 'rt') as f:
    data = f.read()
    print(repr(data))

with open('p01.txt', 'rt', newline='') as f:
    data = f.read()
    print(repr(data))
