#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2020/3/27 21:45
# @File    : p13_summarizing_and_perform_statistics.py
# @Software: PyCharm

"""数据的累加和统计操作"""

import pandas

# read a csv file, skipping last line
data = pandas.read_csv('p13_rats.csv', skipfooter=1)
print(type(data))
print(data)
print()

# investigate range of values for a certain field
print(data['Symbol'].unique())
print()

# filter the data
aa_data = data[data['Symbol'] == 'AA']
print(len(aa_data))
print(aa_data)
print()

# count the value of a field
print(aa_data['Volume'].value_counts())
print()

# group by completion date
data_group_by_date = aa_data.groupby('Date')
print(data_group_by_date)
print(len(data_group_by_date))
for date, data in data_group_by_date:
    print(date)
    print(data)
print()

# Determine counts on each day
date_counts = data_group_by_date.size()
print(date_counts)
print()

# sort the counts
print(date_counts.sort_values())
print()
