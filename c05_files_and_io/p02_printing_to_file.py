#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/8/20 21:41
# @File    : p02_printing_to_file.py
# @Software: PyCharm

# 打印输出至文件中
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c05/p02_printing_to_file.html

with open('p02.txt', 'wt') as f:
    print('hh', file=f)