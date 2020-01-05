#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/8/15 19:09
# @File    : p10_iterate_over_index_value_pairs_of_sequence.py
# @Software: PyCharm

"""序列上索引值迭代"""

from collections import defaultdict

# 使用内置的enumerate函数
items = ['a', 'b', 'c']
for i, val in enumerate(items):
    print(i, val)
print()

# enumerate传递一个开始参数，代表行号从1开始
for i, val in enumerate(items, 1):
    print(i, val)
print()

# 这种情况在遍历文件时想在错误消息中使用行号定位时候非常有用
with open('p10.txt') as f:
    for lineno, line in enumerate(f):
        try:
            int(line)
        except Exception as e:
            print('Line {}: Parse error: {}'.format(lineno, e))
print()

# 将一个文件中出现的单词映射到它出现的行号上
word_summary = defaultdict(list)
with open('p10_2.txt') as f:
    for lineno, line in enumerate(f):
        for word in line.strip().lower().split():
            word_summary[word].append(lineno)
for word, linenos in word_summary.items():
    print(word, linenos)
print()

# 在一个已经解压后的元组序列上使用 enumerate() 函数时容易出错，应该像下面这样写
data = [(1, 2), (3, 4), (5, 6), (7, 8)]
for n, (x, y) in enumerate(data):
    print(n, x, y)
