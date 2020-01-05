#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/8/14 20:42
# @File    : p09_iterate_over_combination_or_permutation.py
# @Software: PyCharm

"""排列组合的迭代"""

from itertools import combinations
from itertools import combinations_with_replacement
from itertools import permutations

# 使用 itertools.permutations() 得到集合中所有元素的排列
items = ['a', 'b', 'c', 'd']
for p in permutations(items):
    print(p)
print()
for p in permutations(items, 2):
    print(p)
print()

# 使用 itertools.combinations 得到集合中所有元素的组合
items = ['a', 'b', 'c']
for c in combinations(items, 3):
    print(c)
print()
for c in combinations(items, 2):
    print(c)
print()

# 函数 itertools.combinations_with_replacement() 允许同一个元素被选择多次
for c in combinations_with_replacement(items, 3):
    print(c)
print()

# 当碰到看上去有些复杂的迭代问题时，可以先看看itertools模块。
# 如果这个问题很普遍，那么很有可能会在里面找到解决方案。
