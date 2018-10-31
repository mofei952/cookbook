#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/10/26 17:42
# @File    : p19_transform_and_reduce_data_same_time.py
# @Software: PyCharm

# 转换并同时计算数据
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c01/p19_transform_and_reduce_data_same_time.html

# 1.使用一个生成器表达式参数
nums = [1, 2, 3, 4, 5]
s = sum(x * x for x in nums)
# 判断一个文件夹中是否有py文件
import os
files = os.listdir('dirname')
if any(name.endswith('.py') for name in files):
    print('There be python!')
else:
    print('Sorry, no python.')
# 将一个元组转换为字符串
s = ('ACME', 50, 123.45)
print(','.join(str(x) for x in s))
# 获取元素的字段值并进行计算
portfolio = [
    {'name':'GOOG', 'shares': 50},
    {'name':'YHOO', 'shares': 75},
    {'name':'AOL', 'shares': 20},
    {'name':'SCOX', 'shares': 65}
]
min_shares = min(s['shares'] for s in portfolio)
# 若要获取整个元素可以这样实现
min_shares2 = min(portfolio, key=lambda s: s['shares'])

