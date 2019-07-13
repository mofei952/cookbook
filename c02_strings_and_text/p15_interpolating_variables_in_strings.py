#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/7/13 19:31
# @File    : p15_interpolating_variables_in_strings.py
# @Software: PyCharm

# 字符串中插入变量
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c02/p15_interpolating_variables_in_strings.html

# 使用字符串的 format() 方法
import string
import sys

s = '{name} has {n} messages.'
print(s.format(name='Guido', n=37))

# 结合使用 format_map() 和 vars()
name = 'Guido'
n = 37
print(s.format_map(vars()))


# vars() 也适用于对象实例
class Info():
    def __init__(self, name, n):
        self.name = name
        self.n = n


info = Info('Guido', 37)
print(s.format_map(vars(info)))


# format 和 format_map() 的一个缺陷就是它们并不能很好的处理变量缺失的情况
# 一种避免这种错误的方法是另外定义一个含有 __missing__() 方法的字典对象
class safesub(dict):
    """防止key找不到"""

    def __missing__(self, key):
        return '{' + key + '}'
del n  # Make sure n is undefined
print(s.format_map(safesub(vars())))


# 如果需要在代码中频繁的执行这些步骤，可以将变量替换步骤用一个工具函数封装起来
def sub(text):
    return text.format_map(safesub(sys._getframe(1).f_locals))
name = 'Guido'
n = 37
print(sub('Hello {name}'))
print(sub('You have {n} messages.'))
print(sub('Your favorite color is {color}'))
