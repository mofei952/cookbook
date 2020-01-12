#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/8/20 21:41
# @File    : p02_printing_to_file.py
# @Software: PyCharm

"""打印输出至文件中"""

# 在 print() 函数中指定file关键字参数可以打印内容到文件中
with open('p02.txt', 'wt') as f:
    print('hh', file=f)

# 文件必须是以文本模式打开。 如果文件是二进制模式的话，打印就会出错。
# with open('p02.txt', 'wb') as f:
#     print('hh', file=f)  # TypeError: a bytes-like object is required, not 'str'
