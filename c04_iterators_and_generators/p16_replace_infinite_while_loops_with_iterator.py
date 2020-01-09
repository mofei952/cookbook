#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/8/19 20:26
# @File    : p16_replace_infinite_while_loops_with_iterator.py
# @Software: PyCharm

"""迭代器代替while无限循环"""

# 常见的IO操作
import sys

with open('p16.txt', 'r') as f:
    while True:
        data = f.read(10)
        if not data:
            break
        print(data, end='')
print()

# 使用iter来进行IO操作
with open('p16.txt', 'r') as f:
    for line in iter(lambda: f.read(10), ''):
        sys.stdout.write(line)

# iter 函数可以接受一个可选的 callable 对象和一个标记(结尾)值作为输入参数。
# 当以这种方式使用的时候，它会创建一个迭代器， 这个迭代器会不断调用 callable 对象直到返回值和标记值相等为止
