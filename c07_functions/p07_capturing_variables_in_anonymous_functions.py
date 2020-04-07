#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/9/1 0:43
# @File    : p07_capturing_variables_in_anonymous_functions.py
# @Software: PyCharm

"""匿名函数捕获变量值"""

x = 10
a = lambda y: x + y
x = 20
b = lambda y: x + y

print(a(10))
print(b(10))

# lambda表达式中的x是一个自由变量，在运行时绑定值，而不是定义时就绑定
x = 15
print(a(10))
x = 3
print(a(10))

# 要让某个匿名函数在定义时就捕获到值，可以将那个参数值定义成默认参数即可
x = 10
a = lambda y, x=x: x + y
x = 20
b = lambda y, x=x: x + y
print(a(10))
print(b(10))
print()

# 通过在一个循环或列表推导中创建一个lambda表达式列表，并期望函数能在定义时就记住每次的迭代值
funcs = [lambda x: x + n for n in range(5)]
for f in funcs:
    print(f(0))
funcs = [lambda x, n=n: x + n for n in range(5)]
for f in funcs:
    print(f(0))
