#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/10/26 17:57
# @File    : p20_combine_multiple_map_to_single_map.py
# @Software: PyCharm

# 合并多个字典或映射
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c01/p20_combine_multiple_map_to_single_map.html

# 1.使用collections 模块中的 ChainMap，先从 a 中找，如果找不到再在 b 中找
a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
from collections import ChainMap, UserDict
c = ChainMap(a, b)
print(c['x'])  # Outputs 1 (from a)
print(c['y'])  # Outputs 2 (from b)
print(c['z'])  # Outputs 3 (from a)

# 对于字典的更新或删除操作总是影响的是列表中第一个字典
c['z'] = 10
c['w'] = 40
del c['x']
print(a)  # {'z': 10, 'w': 40}
# del c['y']  # "Key not found in the first mapping: 'y'"

# 2.使用dict的update方法，此时创建了一个新的字典对象，原字典更新不会放映到新的字典中
a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
merged = dict(b)
merged.update(a)
print(merged['z'])
