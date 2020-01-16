#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2020/1/16 21:15
# @File    : p08_iterate_over_fixed_sized_records.py
# @Software: PyCharm

"""固定大小记录的文件迭代"""

from functools import partial

# 使用iter和partial函数
RECORD_SIZE = 32
with open('p08.data', 'rb') as f:
    records = iter(partial(f.read, RECORD_SIZE), b'')
    for r in records:
        print(r)

# 这个例子中的 records 对象是一个可迭代对象，它会不断的产生固定大小的数据块，直到文件末尾。
# 要注意的是如果总记录大小不是块大小的整数倍的话，最后一个返回元素的字节数会比期望值少。
