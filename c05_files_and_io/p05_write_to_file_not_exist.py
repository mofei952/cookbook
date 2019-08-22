#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/8/22 22:31
# @File    : p05_write_to_file_not_exist.py
# @Software: PyCharm

# 文件不存在才能写入
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c05/p05_write_to_file_not_exist.html

# 在 open() 函数中使用 x 模式来代替 w 模式
# 使用x模式是对写文件时通常会遇到的一个问题的完美解决方案（不小心覆盖了一个已存在的文件）
with open('p05.txt', 'wt') as f:
    f.write('Hello\n')

# with open('p05.txt', 'xt') as f:
#     f.write('Hello\n')
# FileExistsError: [Errno 17] File exists: 'p05.txt'

# 另一种解决方案时先测试这个文件是否存在
import os
if not os.path.exists('p05.txt'):
    with open('p05.txt', 'wt') as f:
        f.write('Hello\n')
else:
    print('File already exists!')

# 显而易见，使用x文件模式更加简单