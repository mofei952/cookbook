#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/8/16 20:25
# @File    : p14_flattening_nested_sequence.py
# @Software: PyCharm

# 展开嵌套的序列
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c04/p14_flattening_nested_sequence.html

# 包含 yield from 语句的递归生成器
from collections import Iterable
def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)
        else:
            yield x
items = [1, 2, [3, 4, [5, 6]], 7, 8]
for x in flatten(items):
    print(x)

# 额外的参数 ignore_types 和检测语句 isinstance(x, ignore_types) 用来将字符串和字节排除在可迭代对象外，
# 防止将它们再展开成单个的字符。
items = ['aa', ['bb', 'cc'], 'dd']
for x in flatten(items):
    print(x)
