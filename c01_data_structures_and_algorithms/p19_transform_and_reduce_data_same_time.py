#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/10/26 17:42
# @File    : p19_transform_and_reduce_data_same_time.py
# @Software: PyCharm

"""转换并同时计算数据"""

# 使用一个生成器表达式参数
nums = [1, 2, 3, 4, 5]
s = sum(x * x for x in nums)

# 判断一个文件夹中是否有py文件
import os
files = os.listdir('.')
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

# 当生成器表达式作为一个单独参数传递给函数时候的巧妙语法（你并不需要多加一个括号）
# 下面这些语句是等效的：
s = sum((x * x for x in nums)) # 显式的传递一个生成器表达式对象
s = sum(x * x for x in nums) # 更加优雅的实现方式，省略了括号

# 使用一个生成器表达式作为参数会比先创建一个临时列表更加高效和优雅。
# 如果你不使用生成器表达式的话，你可能会考虑使用下面的实现方式
# 这种方式同样可以达到想要的效果，但是它会多一个步骤，先创建一个额外的列表。
# 对于小型列表可能没什么关系，但是如果元素数量非常大的时候， 它会创建一个巨大的仅仅被使用一次就被丢弃的临时数据结构。
# 而生成器方案会以迭代的方式转换数据，因此更省内存。
nums = [1, 2, 3, 4, 5]
s = sum([x * x for x in nums])
