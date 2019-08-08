#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/8/8 20:51
# @File    : p03_create_new_iteration_with_generators.py
# @Software: PyCharm

# 使用生成器创建新的迭代模式
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c04/p03_create_new_iteration_with_generators.html

def frange(start, stop, step):
    x = start
    while x < stop:
        yield x
        x += step


for i in frange(1, 10, 2):
    print(i)
print(list(frange(1, 10, 2)))
print(sum(frange(1, 10, 2)))
