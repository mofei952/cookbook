#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/9/1 12:40
# @File    : p08_make_callable_with_fewer_arguments.py
# @Software: PyCharm

"""减少可调用对象的参数个数"""
import logging
import math
from functools import partial

# 使用functools.partial创建偏函数
from multiprocessing.pool import Pool


def spam(a, b, c, d):
    print(a, b, c, d)


s1 = partial(spam, 1)
print(s1)
s1(2, 3, 4)
s1(4, 5, 6)

s2 = partial(spam, d=42)
s2(1, 2, 3)
s2(4, 5, 5)

s3 = partial(spam, 1, 2, d=42)
s3(3)
s3(4)
s3(5)

# 使用partial的例子：根据点和基点之间的距离来排序所有的这些点
points = [(1, 2), (3, 4), (5, 6), (7, 8)]


def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.hypot(x2 - x1, y2 - y1)


pt = (4, 3)
points.sort(key=partial(distance, pt))
print(points)
