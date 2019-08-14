#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/8/14 20:42
# @File    : p09_iterate_over_combination_or_permutation.py
# @Software: PyCharm

# 排列组合的迭代
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c04/p09_iterate_over_combination_or_permutation.html

# 使用 itertools.permutations() 得到集合中所有元素的排列
from itertools import permutations
items = ['a', 'b', 'c', 'd']
for p in permutations(items):
    print(p)
for p in permutations(items, 2):
    print(p)

# 使用 itertools.combinations 得到集合中所有元素的组合
from itertools import combinations
items = ['a', 'b', 'c']
for c in combinations(items, 3):
    print(c)
for c in combinations(items, 2):
    print(c)

# 函数 itertools.combinations_with_replacement() 允许同一个元素被选择多次
from itertools import combinations_with_replacement
for c in combinations_with_replacement(items, 3):
    print(c)

# 当碰到看上去有些复杂的迭代问题时，可以先看看itertools模块。
# 如果这个问题很普遍，那么很有可能会在里面找到解决方案