#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/8/29 20:22
# @File    : p05_define_functions_with_default_arguments.py
# @Software: PyCharm

"""定义有默认参数的函数"""


# 将可选参数放在参数列最后，并指定默认值
def foo(a, b=11):
    print(a, b)


foo(1)
foo(1, 2)
print()


# 默认参数是可变参数（列表，集合，字典）时，可以使用None作为默认值
def foo2(a, b=None):
    if b is None:
        b = []
    print(a, len(b))


foo2(1)
foo2(1, [1, 2])
print()


# 默认参数不要直接使用可变对象
# 如果使用可变对象，当默认值在其他地方被修改将会带来很多麻烦，这些修改会影响到下次调用是这个函数的默认值
def foo5(a, b=[]):
    return b


x = foo5(1)
print(x)
x.append(2)
y = foo5(1)
print(y)
print()

# 如果不想提供默认值，仅仅是测试某个默认参数是否有传递进来，可以使用一个独一无二的私有对象实例
_no_value = object()


def foo3(a, b=_no_value):
    if b is _no_value:
        print('No parameter b')
        return
    print(a, b)


foo3(1)
foo3(1, 3)
print()

# 默认参数的值仅仅在函数定义的时候赋值一次
x = 1


def foo4(a, b=x):
    print(a, b)


foo4(2)
x = 3
foo4(2)
