#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/8/19 19:52
# @File    : p15_iterate_in_sorted_order_over_merged_sorted_iterables.py
# @Software: PyCharm

# 顺序迭代合并后的排序迭代对象
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c04/p15_iterate_in_sorted_order_over_merged_sorted_iterables.html

import heapq

a = [1, 4, 7, 10]
b = [2, 5, 6, 11]
for i in heapq.merge(a, b):
    print(i)

# heapq.merge 可迭代特性意味着它不会立马读取所有序列。
# 这就意味着可以在非常长的序列中使用，而不会有太大的开销

# heapq.merge() 需要所有输入序列必须是排过序的。
# 它并不会预先读取所有数据到堆栈中或者预先排序，也不会对输入做任何的排序检测。
# 它仅仅是检查所有序列的开始部分并返回最小的那个，这个过程一直会持续直到所有输入序列中的元素都被遍历完。