#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/8/27 22:07
# @File    : p03_attach_informatinal_matadata_to_function_arguments.py
# @Software: PyCharm

"""给函数参数增加元信息"""


# 使用函数参数注解，为函数添加一些额外信息。
# python解释器不会对这些注解添加任何的语义。它们不会被类型检查，运行时跟没有加注解之前的效果也没有任何差距。

def add(a: int, b: int) -> int:
    return a + b


# 函数注解能提示程序员应该怎样正确使用这个函数。
# 第三方工具和框架可能会对这些注解添加语义，同时它们也会出现在文档中。
help(add)

# 函数注解只存储在函数的 __annotations__ 属性中。
print(add.__annotations__)
