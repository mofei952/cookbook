#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/6/26 8:48
# @File    : p15_group_records_based_on_field.py
# @Software: PyCharm

"""通过某个字段将记录分组"""

from collections import defaultdict
from itertools import groupby
from operator import itemgetter

rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]

# 使用itertools.groupby() 函数将数据分组
# groupby()仅仅检查连续的数据，如果没有排序过的话，可能得不到想要的结果
rows.sort(key=itemgetter('date'))
for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for i in items:
        print(' ', i)

# 如果仅仅只是想根据 date 字段将数据分组到一个大的数据结构中去，并且允许随机访问，
# 最好使用 defaultdict() 来构建一个多值字典，这样能对每个指定日期访问对应的记录。
# 这种方式不用先排序，会比先排序然后再通过 groupby() 函数迭代的方式运行得快一些。
rows_by_date = defaultdict(list)
for row in rows:
    rows_by_date[row['date']].append(row)

for r in rows_by_date['07/01/2012']:
    print(r)
