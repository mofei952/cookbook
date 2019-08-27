#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/8/27 22:07
# @File    : p03_attach_informatinal_matadata_to_function_arguments.py
# @Software: PyCharm

# 给函数参数增加元信息
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c07/p03_attach_informatinal_matadata_to_function_arguments.html

# 使用函数参数注解，为函数添加一些额外信息

def add(a: int, b: int) -> int:
    return a + b


help(add)
print(add.__annotations__)

# 尽管注解的使用方法可能有很多种，但是它们的主要用途还是文档。
# 因为python并没有类型声明，通常来讲仅仅通过阅读源码很难知道应该传递什么样的参数给这个函数。
# 这时候使用注解就能给程序员更多的提示，让他们可以正确的使用函数。
