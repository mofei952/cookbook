#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/10/26 17:05
# @File    : p17_extract_subset_of_dict.py
# @Software: PyCharm

# 从字典中提取子集
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c01/p17_extract_subset_of_dict.html

# 使用字典推导式
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

# 筛选出价格大于200的内容
p1 = {key: value for key, value in prices.items() if value > 200}

# 筛选已知名称的内容
tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
p2 = {key: value for key, value in prices.items() if key in tech_names}

# 另一种写法，比上面的写法慢
tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
p3 = {key: prices[key] for key in prices.keys() & tech_names}
