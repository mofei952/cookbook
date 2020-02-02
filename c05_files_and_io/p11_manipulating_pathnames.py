#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2020/1/31 23:03
# @File    : p11_manipulating_pathnames.py
# @Software: PyCharm

"""文件路径名的操作"""

import os

# 使用os.path模块中的函数来操作路径名
path = '/Users/beazley/Data/data.csv'
print(os.path.basename(path))
print(os.path.dirname(path))
print(os.path.join('tmp', 'data', os.path.basename(path)))

path = '~/Data/data.csv'
print(os.path.expanduser(path))
print(os.path.splitext(path))

# os.path 模块知道Unix和Windows系统之间的差异并且能够可靠地处理类似 Data/data.csv 和 Data\data.csv 这样的文件名
