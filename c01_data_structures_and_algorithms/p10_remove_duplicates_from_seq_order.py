#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/6/24 18:16
# @File    : p10_remove_duplicates_from_seq_order.py
# @Software: PyCharm

# 删除序列相同元素并保持顺序
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c01/p10_remove_duplicates_from_seq_order.html

# 如果序列上的值都是 hashable 类型，那么可以很简单的利用集合和生成器来解决这个问题
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)
a = [1, 5, 2, 1, 9, 1, 5, 10]
print(list(dedupe(a)))


# 消除元素不可哈希（比如 dict 类型）的序列中重复元素
def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)
a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
print(list(dedupe(a, key=lambda d: (d['x'], d['y']))))
print(list(dedupe(a, key=lambda d: d['x'])))

# 使用set方法不能维护元素的顺序，生成的结果中的元素位置被打乱
# 使用生成器函数可以让函数更加通用，不仅仅是局限于列表处理。可以直接处理文件
# key函数参数模仿了 sorted() , min() 和 max() 等内置函数的相似功能
with open('p10_remove_duplicates_from_seq_order.txt', 'r') as f:
    for line in dedupe(f):
        print(line, end='')
