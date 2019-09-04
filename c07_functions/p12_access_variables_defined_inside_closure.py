#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/9/4 21:13
# @File    : p12_access_variables_defined_inside_closure.py
# @Software: PyCharm

# 访问闭包中定义的变量
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c07/p12_access_variables_defined_inside_closure.html

# 通过编写访问函数并将其作为函数属性绑定到闭包上来实现
# nonlocal 声明可以让我们编写函数来修改内部变量的值
# 函数属性允许我们用一种很简单的方式将访问方法绑定到闭包函数上
def sample():
    n = 0

    def func():
        print('n =', n)

    def get_n():
        return n

    def set_n(value):
        nonlocal n
        n = value

    func.get_n = get_n
    func.set_n = set_n
    return func


f = sample()
f()
f.set_n(10)
f()
print(f.get_n())





# 还可以让闭包模拟类的实例
import sys


class ClosureInstance:
    def __init__(self, locals=None):
        if locals is None:
            locals = sys._getframe(1).f_locals

        # Update instance dictionary with callables
        self.__dict__.update((key, value) for key, value in locals.items()
                             if callable(value))

    # Redirect special methods
    def __len__(self):
        return self.__dict__['__len__']()


# Example use
def Stack():
    items = []

    def push(item):
        items.append(item)

    def pop():
        return items.pop()

    def __len__():
        return len(items)

    return ClosureInstance()


s = Stack()
print(s)
s.push(10)
s.push(20)
s.push('Hello')
print(len(s))
print(s.pop())
print(s.pop())
print(s.pop())
