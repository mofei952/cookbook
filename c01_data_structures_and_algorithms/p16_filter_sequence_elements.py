#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/7/2 18:23
# @File    : p16_filter_sequence_elements.py
# @Software: PyCharm


# 过滤序列元素
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c01/p16_filter_sequence_elements.html

# 使用列表推导
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
print([n for n in mylist if n > 0])

# 使用列表推导的一个潜在缺陷就是如果输入非常大的时候会产生一个非常大的结果集，占用大量内存。
# 如果对内存比较敏感，那么可以使用生成器表达式迭代产生过滤的元素。
pos = (n for n in mylist if n > 0)
for x in pos:
    print(x)

# 若过滤规则比较复杂，不能简单的在列表推导或者生成器表达式中表达出来，可以使用内建的 filter() 函数
# filter() 函数返回了一个迭代器，可以通过list（）方法转换为列表
values = ['1', '2', '-3', '-', '4', 'N/A', '5']
def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False
ivals = list(filter(is_int, values))
print(ivals)

# 过滤操作的一个变种就是将不符合条件的值用新的值代替，而不是丢弃它们。
clip_neg = [n if n > 0 else 0 for n in mylist]
print(clip_neg)
clip_pos = [n if n < 0 else 0 for n in mylist]
print(clip_pos)

# 另外一个值得关注过滤工具就是 itertools.compress() ，
# 它以一个 iterable 对象和一个相对应的 Boolean 选择器序列作为输入参数。
# 然后输出 iterable 对象中对应选择器为 True 的元素。
# 当你需要用另外一个相关联的序列来过滤某个序列的时候，这个函数是非常有用的
addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]
counts = [0, 3, 10, 4, 1, 7, 6, 1]
from itertools import compress

more5 = [n > 5 for n in counts]
print(more5)
print(list(compress(addresses, more5)))