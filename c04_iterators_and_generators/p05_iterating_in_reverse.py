#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/8/10 20:58
# @File    : p05_iterating_in_reverse.py
# @Software: PyCharm

# 反向迭代
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c04/p05_iterating_in_reverse.html

# 使用内置的 reversed() 函数
a = [1, 2, 3, 4, 5]
for i in reversed(a):
    print(i)

# 反向迭代仅仅当对象的大小可预先确定或者对象实现了 __reversed__() 的特殊方法时才能生效。
# 如果两者都不符合，那你必须先将对象转换为一个列表才行
# 如果可迭代对象元素很多的话，将其预先转换为一个列表要消耗大量的内存
f = open('p05_iterating_in_reverse.txt')
for line in reversed(list(f)):
    print(line, end='')


# 自定义类上实现 __reversed__() 方法来实现反向迭代
class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1


for i in Countdown(10):
    print(i)
for i in reversed(Countdown(10)):
    print(i)

# 定义一个反向迭代器可以使得代码非常的高效
# 因为它不再需要将数据填充到一个列表中然后再去反向迭代这个列表