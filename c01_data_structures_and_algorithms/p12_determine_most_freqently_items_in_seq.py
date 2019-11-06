#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/6/25 19:09
# @File    : p12_determine_most_freqently_items_in_seq.py
# @Software: PyCharm

"""序列中出现次数最多的元素"""

from collections import Counter

# 单词列表
words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

# 使用collections.Counter和most_common()找出频率最高的3个单词
word_counts = Counter(words)
top_three = word_counts.most_common(3)
print(top_three)

# Counter 对象可以接受任意的由可哈希（hashable）元素构成的序列对象
# Counter 其实是dict的子类，将元素映射到它出现的次数上
print(word_counts['look'])
print(word_counts['under'])

# 对Counter对象手动增加计数
morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']
for word in morewords:
    word_counts[word] += 1
print(word_counts)

# 或者可以使用 Counter的update() 方法：
word_counts.update(morewords)
print(word_counts)

# 它们可以很容易的跟数学运算操作相结合
a = Counter(words)
b = Counter(morewords)
c = a + b
print(c)
d = a - b
print(d)
