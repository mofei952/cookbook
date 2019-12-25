#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/8/8 20:51
# @File    : p03_create_new_iteration_with_generators.py
# @Software: PyCharm

"""使用生成器创建新的迭代模式"""
def frange(start, stop, step):
    x = start
    while x < stop:
        yield x
        x += step


# 可以用for循环迭代它或者使用其他接受一个可迭代对象的函数
for i in frange(1, 3, 0.5):
    print(i)
print(list(frange(1, 10, 2)))
print(sum(frange(1, 10, 2)))

# 生成器函数的底层工作机制
f = frange(1, 6, 2)  # Create the generator, notice no output appears
print(f)
print(next(f))  # Run to first yield and emit a value
print(next(f))  # Run to the next yield
print(next(f))  # Run to the next yield
# print(next(f)) # Run to next yield (iteration stops)
