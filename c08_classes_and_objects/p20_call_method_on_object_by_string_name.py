#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/9/26 21:13
# @File    : p20_call_method_on_object_by_string_name.py
# @Software: PyCharm

"""通过字符串调用对象方法"""

import math
import operator


# 可用使用getattr()
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point({!r:},{!r:})'.format(self.x, self.y)

    def distance(self, x, y):
        return math.hypot(self.x - x, self.y - y)


p = Point(3, 4)
d = getattr(p, 'distance')(0, 0)
print(d)

# 使用operator.methodcaller()
distance = operator.methodcaller('distance', 0, 0)(p)
print(distance)

# 通过相同的参数多次调用某个方法时，可以使用methodcaller
points = [
    Point(1, 2),
    Point(3, 0),
    Point(10, -3),
    Point(-5, -7),
    Point(-1, 8),
    Point(3, 2)
]
points.sort(key=operator.methodcaller('distance', 0, 0))
print(points)
