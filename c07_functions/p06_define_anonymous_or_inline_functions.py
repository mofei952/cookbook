#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/8/31 22:52
# @File    : p06_define_anonymous_or_inline_functions.py
# @Software: PyCharm

# 定义匿名或内联函数
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c07/p06_define_anonymous_or_inline_functions.html

# 使用lambda表达式
add = lambda x, y: x + y
print(add(1, 2))
print(add('hello', 'world'))

# lambda表达式典型的使用场景是排序或数据reduce
names = ['David Beazley', 'Brian Jones',
         'Raymond Hettinger', 'Ned Batchelder']
print(sorted(names, key=lambda name: name.split()[-1].lower()))

# 尽管lambda表达式允许定义简单函数，但是它的使用是有限制的
# 你只能指定单个表达式，它的值就是最后的返回值
# 当编写大量计算表达式值的短小函数或者需要用户提供回调函数的程序的时候，就会用到lambda表达式