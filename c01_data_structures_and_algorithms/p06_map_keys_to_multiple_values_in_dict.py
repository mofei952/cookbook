#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/6/22 13:46
# @File    : p06_map_keys_to_multiple_values_in_dict.py
# @Software: PyCharm

"""字典中的键映射多个值"""

from collections import defaultdict

# 要让字典中的一个键映射多个值，可以使用defaultdict
# defaultdict 会自动为将要访问的键（就算目前字典中并不存在这样的键）创建映射实体
d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
print(d)

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)
print(d)

# 如果你不需要这样的特性，可以在一个普通的字典上使用 setdefault() 方法来代替。
# 但这样每次调用都得创建一个新的初始值的实例（例子程序中的空列表 [] ），会有点别扭
d = {}  # 一个普通的字典
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('b', []).append(4)
print(d)

# 使用 defaultdict 的话代码比普通方式更加简洁
pairs = [('a', 1), ('a', 2), ('b', 1)]
d = {}
for key, value in pairs:
    if key not in d:
        d[key] = []
    d[key].append(value)
print(d)
d = defaultdict(list)
for key, value in pairs:
    d[key].append(value)
print(d)
