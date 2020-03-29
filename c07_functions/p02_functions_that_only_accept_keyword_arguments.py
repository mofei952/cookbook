#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/8/27 19:10
# @File    : p02_functions_that_only_accept_keyword_arguments.py
# @Software: PyCharm

"""只接受关键字参数的函数"""


# 要让函数的某些参数强制使用关键字参数传递，将强制关键字参数放在某个*参数或者某个*后面就可以实现
# 使用强制关键字参数会比使用位置参数表意更加清晰，程序也更加具有可读性
def recv(maxsize, *, block):
    """Receives a message"""
    pass


# recv(1024, True)  # TypeError: recv() takes 1 positional argument but 2 were given
recv(1024, block=True)


# 可以在接受任意多个位置参数的函数中指定关键字参数
def minimum(*values, clip=None):
    m = min(values)
    if clip is not None:
        m = clip if clip > m else m
    return m


print(minimum(1, 2, 3, -5))
print(minimum(1, 2, 3 - 5, clip=0))

# 使用强制关键字参数也会比使用**kwargs参数更好，因为在使用函数help的时候输出也会更容易理解
help(recv)
