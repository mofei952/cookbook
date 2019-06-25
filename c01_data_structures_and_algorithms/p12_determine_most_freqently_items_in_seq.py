#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/6/25 19:09
# @File    : p12_determine_most_freqently_items_in_seq.py
# @Software: PyCharm

# 序列中出现次数最多的元素
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c01/p12_determine_most_freqently_items_in_seq.html

# 使用collections.Counter和most_common()找出哪个单词出现频率最高
words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]
from collections import Counter

word_counts = Counter(words)
# 出现频率最高的3个单词
top_three = word_counts.most_common(3)
print(top_three)
# Outputs [('eyes', 8), ('the', 5), ('look', 4)]

# Counter 对象可以接受任意的由可哈希（hashable）元素构成的序列对象

# 手动增加计数
morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']
# for word in morewords:
#     word_counts[word] += 1
# print(word_counts)

# 或者可以使用 Counter的update() 方法：
word_counts.update(morewords)
print(word_counts)

# 它们可以很容易的跟数学运算操作相结合
a = Counter(words)
b = Counter(morewords)
# Combine counts
c = a + b
print(c)
# Subtract counts
d = a - b
print(d)
