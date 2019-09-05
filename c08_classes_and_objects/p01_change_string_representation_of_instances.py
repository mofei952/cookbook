#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/9/4 21:41
# @File    : p01_change_string_representation_of_instances.py
# @Software: PyCharm

# 改变对象的字符串显示
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c08/p01_change_string_representation_of_instances.html

# 使对象实例的打印更具可读性
class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Pair({0.x!r}, {0.y!r})'.format(self)

    def __str__(self):
        return '({0.x!r}, {0.y!r})'.format(self)


# __repr__() 方法返回一个实例的代码表示形式，通常用来重新构造这个实例。
# 内置的 repr() 函数返回这个字符串，跟使用交互式解释器显示的值是一样的。
# __str__() 方法将实例转换为一个字符串，使用 str() 或 print() 函数会输出这个字符串
# 如果 __str__() 没有被定义，那么就会使用 __repr__() 来代替输出。
p = Pair(3, 4)
print(p)
print(repr(p))

# !r 格式化代码指明输出使用 __repr__() 来代替默认的 __str__()
p = Pair(3, 4)
print('p is {0!r}'.format(p))
print('p is {0}'.format(p))

# 格式化代码 {0.x} 对应的是第1个参数的x属性
print('Pair({0.x!r}, {0.y!r})'.format(p))
# 也可以使用%操作符
print('Pair(%r, %r)' % (p.x, p.y))

# __repr__() 生成的文本字符串标准做法是需要让 eval(repr(x)) == x 为真。
# 如果实在不能这样子做，应该创建一个有用的文本表示，并使用 < 和 > 括起来
f = open('p01_change_string_representation_of_instances.py')
print(repr(f))
