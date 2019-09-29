#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/9/29 19:35
# @File    : p23_managing_memory_in_cyclic_data_structures.py
# @Software: PyCharm

# 循环引用数据结构的内存管理
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c08/p23_managing_memory_in_cyclic_data_structures.html

import weakref


# 循环引用会导致垃圾对象不会被回收
class Data:
    def __del__(self):
        print('Data.__del__')


class Node:
    def __init__(self):
        self.data = Data()
        self.parent = None
        self.children = []

    def add_child(self, child):
        self.children.append(child)
        child.parent = self


a = Data()
del a  # Immediately deleted
a = Node()
del a  # Immediately deleted
a = Node()
a.add_child(Node())
del a  # Not deleted


# 使用弱引用可以消除循环引用的问题
class Node:
    def __init__(self, value):
        self.data = Data()
        self.value = value
        self._parent = None
        self.children = []

    def __repr__(self):
        return 'Node({!r:})'.format(self.value)

    # property that manages the parent as a weak-reference
    @property
    def parent(self):
        return None if self._parent is None else self._parent()

    @parent.setter
    def parent(self, node):
        self._parent = weakref.ref(node)

    def add_child(self, child):
        self.children.append(child)
        child.parent = self


a = Node(1)
a.add_child(Node(2))
del a  # Immediately deleted

root = Node('parent')
c1 = Node('child')
root.add_child(c1)
print(c1.parent)
del root
print(c1.parent)
