#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/8/15 19:09
# @File    : p10_iterate_over_index_value_pairs_of_sequence.py
# @Software: PyCharm

# 序列上索引值迭代
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c04/p10_iterate_over_index_value_pairs_of_sequence.html

# 使用内置的enumerate函数
items = ['a', 'b', 'c']
for i, val in enumerate(items):
    print(i, val)

# enumerate传递一个开始参数，代表行号从1开始
for i, val in enumerate(items, 1):
    print(i, val)

# 这种情况在遍历文件时想在错误消息中使用行号定位时候非常有用
with open('p10_iterate_over_index_value_pairs_of_sequence.txt') as f:
    for lineno, line in enumerate(f):
        try:
            int(line)
        except Exception as e:
            print(lineno, e)

# 将一个文件中出现的单词映射到它出现的行号上
from collections import defaultdict
word_summary = defaultdict(list)
with open('p10_iterate_over_index_value_pairs_of_sequence2.txt') as f:
    for lineno, line in enumerate(f):
        for word in line.strip().lower().split():
            word_summary[word].append(lineno)
print(word_summary)
