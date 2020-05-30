#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/9/30 21:28
# @File    : p24_making_classes_support_comparison_operations.py
# @Software: PyCharm

"""让类支持比较操作"""

from functools import total_ordering


# 如果要实现所有的比较方法会比较麻烦，装饰器 functools.total_ordering 可以简化这个处理的
# 只需定义一个 __eq__() 方法， 外加其他方法(__lt__, __le__, __gt__, __ge__)中的一个，然后total_ordering装饰器会自动为你填充其它比较方法
class Room:
    def __init__(self, name, length, width):
        self.name = name
        self.length = length
        self.width = width
        self.square_feet = self.length * self.width


@total_ordering
class House:
    def __init__(self, name, style):
        self.name = name
        self.style = style
        self.rooms = list()

    @property
    def living_space_footage(self):
        return sum(r.square_feet for r in self.rooms)

    def add_room(self, room):
        self.rooms.append(room)

    def __str__(self):
        return '{}: {} square foot {}'.format(self.name, self.living_space_footage, self.style)

    def __eq__(self, other):
        return self.living_space_footage == other.living_space_footage

    def __lt__(self, other):
        return self.living_space_footage < other.living_space_footage


h1 = House('h1', 'Cape')
h1.add_room(Room('Master Bedroom', 14, 21))
h1.add_room(Room('Living Room', 18, 20))
h1.add_room(Room('Kitchen', 12, 16))
h1.add_room(Room('Office', 12, 12))

h2 = House('h2', 'Ranch')
h2.add_room(Room('Master Bedroom', 14, 21))
h2.add_room(Room('Living Room', 18, 20))
h2.add_room(Room('Kitchen', 12, 16))

h3 = House('h3', 'Split')
h3.add_room(Room('Master Bedroom', 14, 21))
h3.add_room(Room('Living Room', 18, 20))
h3.add_room(Room('Office', 12, 16))
h3.add_room(Room('Kitchen', 15, 17))

print(h1)
print(h2)
print(h3)
print()

print(h1 < h2)
print(h1 > h2)
print(h1 >= h2)
print()

houses = [h1, h2, h3]
print(max(houses))
print(min(houses))
