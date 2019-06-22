#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/6/22 14:00
# @File    : p07_keep_dict_in_order.py
# @Software: PyCharm

# 字典排序
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c01/p07_keep_dict_in_order.html


# 使用collections 模块中的 OrderedDict 类
# 在迭代操作的时候它会保持元素被插入时的顺序
import random
from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4
# Outputs "foo 1", "bar 2", "spam 3", "grok 4"
for key in d:
    print(key, d[key])

# 需要序列化或编码成其他格式的映射的时候， OrderedDict 是非常有用的。
# 比如，想精确控制以 JSON 编码后字段的顺序，可以先使用 OrderedDict 来构建这样的数据
import json

print(json.dumps(d))

# python3.6及后续版本的dict为有序
t = {1: 1, 3: 1, 4: 1, 5: 1, 2: 1}
for k, v in t.items():
    print(k)

# OrderedDict 内部维护着一个根据键插入顺序排序的双向链表。
# 每次当一个新的元素插入进来的时候， 它会被放到链表的尾部。对于一个已经存在的键的重复赋值不会改变键的顺序。

# 一个 OrderedDict 的大小是一个普通字典的两倍，因为它内部维护着另外一个链表。
# 所以如果要构建一个需要大量 OrderedDict 实例的数据结构的时候（比如读取 100,000 行 CSV 数据到一个 OrderedDict 列表中去），
# 那么得仔细权衡一下是否使用 OrderedDict 带来的好处要大过额外内存消耗的影响。
