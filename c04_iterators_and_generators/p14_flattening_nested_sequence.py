#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/8/16 20:25
# @File    : p14_flattening_nested_sequence.py
# @Software: PyCharm

"""展开嵌套的序列"""

from collections import Iterable


# 定义一个包含 yield from 语句的递归生成器，yield from 就会返回所有子例程的值
def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x, ignore_types)
        else:
            yield x


items = [1, 2, [3, 4, [5, 6]], 7, 8]
for x in flatten(items):
    print(x)

# 额外的参数 ignore_types 和检测语句 isinstance(x, ignore_types) 用来将字符串和字节排除在可迭代对象外，防止将它们再展开成单个的字符。
# 这样字符串数组就可以返回期望的结果了。
items = ['aa', ['bb', 'cc'], 'dd']
for x in flatten(items):
    print(x)

# 可以将tuple作为一个不可展开的类型
items = [(1, 2), [(3, 4), (5, 6)], (7, 8)]
for x in flatten(items, ignore_types=(tuple)):
    print(x)
