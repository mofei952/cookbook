#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/8/14 20:11
# @File    : p08_skip_first_part_of_iterable.py
# @Software: PyCharm

# 跳过可迭代对象的开始部分
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c04/p08_skip_first_part_of_iterable.html

# 使用 itertools.dropwhile() 函数
with open('p08_skip_first_part_of_iterable.txt') as f:
    for line in f:
        print(line, end='')
print()
from itertools import dropwhile
with open('p08_skip_first_part_of_iterable.txt') as f:
    for line in dropwhile(lambda line: line.startswith('#'), f):
        print(line, end='')
print()

# 已经知道了要跳过的元素的个数的话，那么可以使用 itertools.islice() 来代替
from itertools import islice
items = ['a', 'b', 'c', 1, 4, 10, 15]
for x in islice(items, 3, None):
    print(x)
for x in islice(items, None, 3):
    print(x)

# 通常的过滤写法，会过滤所有符合条件的行，不只是开始部分
with open('p08_skip_first_part_of_iterable.txt') as f:
    lines = (line for line in f if not line.startswith('#'))
    for line in lines:
        print(line, end='')