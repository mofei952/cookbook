#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/6/23 16:16
# @File    : p08_calculating_with_dict.py
# @Software: PyCharm

"""字典的运算，求最小值、最大值、排序等等"""

from operator import itemgetter

# 股票名和价格映射字典
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

# 为了对字典值执行计算操作，通常需要使用 zip() 函数先将键和值反转过来
# 当多个实体拥有相同的值的时候，键会决定返回结果
min_price = min(zip(prices.values(), prices.keys()))
print(min_price)
max_price = max(zip(prices.values(), prices.keys()))
print(max_price)
prices_sorted = sorted(zip(prices.values(), prices.keys()))
print(prices_sorted)

# 执行这些计算的时候，需要注意的是 zip() 函数创建的是一个只能访问一次的迭代器。
# 比如，下面的代码就会产生错误：
prices_and_names = zip(prices.values(), prices.keys())
print(min(prices_and_names))  # OK
# print(max(prices_and_names))  # ValueError: max() arg is an empty sequence

# 可以在 min() 和 max() 函数中提供 key 函数参数来获取最小值或最大值对应的键的信息
min_price = min(prices, key=lambda k: prices[k])  # Returns 'FB'
print(min_price)
max_price = max(prices, key=lambda k: prices[k])  # Returns 'AAPL'
print(max_price)

# 在 min() 和 max() 函数中提供 key 函数参数来获取最小值或最大值对应的键和值的信息
min_price = min(prices.items(), key=lambda item: (item[1], item[0]))
print(min_price)
max_price = max(prices.items(), key=itemgetter(1, 0))
print(max_price)
