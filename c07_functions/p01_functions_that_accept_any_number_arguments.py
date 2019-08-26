#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/8/26 21:04
# @File    : p01_functions_that_accept_any_number_arguments.py
# @Software: PyCharm

# 可接受任意数量参数的函数
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c07/p01_functions_that_accept_any_number_arguments.html

# 让一个函数接受任意数量的位置参数，可以使用*参数
def avg(first, *rest):
    return (first + sum(rest)) / (1 + len(rest))

print(avg(1.5, 2.5))
print(avg(1, 2, 3, 4))

# 让函数接受任意数量的关键字参数，可以使用**开头的参数
import html
def make_element(name, value, **attrs):
    attr_str = ' '.join('{}="{}"'.format(k,v) for k,v in attrs.items())
    element = '<{name} {attrs}>{value}</{name}>'.format(name=name, attrs=attr_str, value=(html.escape(value)))
    return element

print(make_element('item', 'aaa', size='large', quantity=6))
print(make_element('p', '<spam>'))

# 同时接受任意数量的位置参数和关键字参数，可以同时使用*和**参数
def anyargs(*args, **kwargs):
    print(args) # A tuple
    print(kwargs) # A dict

# 一个*参数只能出现在函数定义中最后一个位置参数后面，而**参数只能出现在最后一个参数。
# 有一点要注意的是，在*参数后面仍然可以定义其他参数。这种参数就是所谓的强制关键字参数
def a(x, *args, y):
    pass

def b(x, *args, y, **kwargs):
    pass