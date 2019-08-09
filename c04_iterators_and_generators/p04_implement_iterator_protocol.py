#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/8/9 20:46
# @File    : p04_implement_iterator_protocol.py
# @Software: PyCharm

# 实现迭代器协议
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c04/p04_implement_iterator_protocol.html

# 实现一个以深度优先方式遍历树形节点的生成器
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

    def depth_first(self):
        yield self
        for node in self:
            yield from node.depth_first()

if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(Node(3))
    child1.add_child(Node(4))
    child2.add_child(Node(5))

    for node in root.depth_first():
        print(node)














