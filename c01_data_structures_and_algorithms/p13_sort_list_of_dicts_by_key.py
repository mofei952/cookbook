#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/6/25 19:36
# @File    : p13_sort_list_of_dicts_by_key.py
# @Software: PyCharm

"""通过某个关键字排序一个字典列表"""

from operator import itemgetter

# 字典列表
rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

# 使用 operator 模块的 itemgetter 函数
# itemgetter函数会创建一个calleable对象，用于从元素中获取用来排序的值
rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))
print(rows_by_fname)
print(rows_by_uid)

# itemgetter() 函数也支持多个 keys
# 参数可以是一个字典键名称， 一个整形值或者任何能够传入一个对象的 __getitem__() 方法的值
# 如果传入多个索引参数给 itemgetter() ，它生成的 callable 对象会返回一个包含所有元素值的元组
rows_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))
print(rows_by_lfname)

# itemgetter() 也可以用 lambda 表达式代替
rows_by_fname = sorted(rows, key=lambda r: r['fname'])
rows_by_lfname = sorted(rows, key=lambda r: (r['lname'], r['fname']))

# 以上用法同样适用于 min() 和 max() 等函数
min_row = min(rows, key=itemgetter('uid'))
max_row = max(rows, key=itemgetter('uid'))
print(min_row)
print(max_row)
