#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/8/8 19:31
# @File    : p02_delegating_iteration.py
# @Software: PyCharm

# 代理迭代
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c04/p02_delegating_iteration.html

# 对自定义容器对象执行迭代操作
class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

if __name__ == '__main__':
    root = Node(0)
    root.add_child(Node(1))
    root.add_child(Node(2))
    for child in root:
        print(child)
















