#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/8/6 21:16
# @File    : p01_manually_consuming_iterator.py
# @Software: PyCharm

"""手动遍历迭代器"""

# 使用 next() 函数并在代码中捕获 StopIteration 异常
with open('p01.txt') as f:
    try:
        while True:
            line = next(f)
            print(line, end='')
    except StopIteration:
        pass

# 可以通过返回一个指定值来标记结尾，比如 None
with open('p01.txt') as f:
    while True:
        line = next(f, None)
        if line is None:
            break
        print(line, end='')

# 迭代过程
items = [1, 2, 3]
it = iter(items)  # 调用 items.__iter__()
print(next(it))  # 调用 it.__next__()
print(next(it))
print(next(it))
# print(next(it)) # 抛出 StopIteration
