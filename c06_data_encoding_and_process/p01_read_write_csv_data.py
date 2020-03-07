#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2020/3/7 18:12
# @File    : p01_read_write_csv_data.py
# @Software: PyCharm

"""读写csv数据"""

import csv
import re
from collections import namedtuple

# 使用csv模块读取csv数据
data = []
with open('p01.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
        data.append(row)

print(headers)
for row in data:
    print(row)
print()

# 可以使用row[0]访问Symbol，row[4]访问Change
# 由于这种下标访问通常会引起混淆，所有可以考虑使用命名元组
with open('p01.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    Row = namedtuple('Row', headers)
    for r in f_csv:
        row = Row(*r)
        print(row.Symbol, row.Change)
print()

# 另一种方式是将数据读取到一个字典序列中去
with open('p01.csv') as f:
    f_csv = csv.DictReader(f)
    for row in f_csv:
        print(row['Symbol'], row['Change'])
print()

# 使用csv模块的writer对象 进行csv写入
with open('p01.csv', 'w', newline='') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(data)

# 写入字典序列的数据
headers = ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']
rows = [
    {'Symbol': 'AA', 'Price': 39.48, 'Date': '6/11/2007', 'Time': '9:36am', 'Change': -0.18, 'Volume': 181800},
    {'Symbol': 'AIG', 'Price': 71.38, 'Date': '6/11/2007', 'Time': '9:36am', 'Change': -0.15, 'Volume': 195500},
    {'Symbol': 'AXP', 'Price': 62.58, 'Date': '6/11/2007', 'Time': '9:36am', 'Change': -0.46, 'Volume': 935000},
]
with open('p01.csv', 'w', newline='') as f:
    f_csv = csv.DictWriter(f, headers)
    f_csv.writeheader()
    f_csv.writerows(rows)

# 可以使用csv模块来读取以tab分割的数据
with open('p01_2.csv', 'w') as f:
    for row in data:
        f.write('\t'.join(row) + '\n')

with open('p01_2.csv') as f:
    f_tsv = csv.reader(f, delimiter='\t')
    for row in f_tsv:
        print(row)
print()

# 读取csv数据并将它们转换为命名元组，需要注意对列名进行合法性认证
with open('p01_3.csv') as f:
    f_csv = csv.reader(f)
    headers = [re.sub('[^a-zA-Z_\d]', '_', h) for h in next(f_csv)]
    Row = namedtuple('Row', headers, rename=True)
    for r in f_csv:
        row = Row(*r)
        print(row)
print()

# csv产生的数据都是字符串类型的，它不会做任何其他类型的转换
# 如果需要的话，可以手动实现
col_types = [str, float, str, str, float, int]
with open('p01.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
        row = tuple(convert(value) for convert, value in zip(col_types, row))
        print(row)
print()

# 也可以转换字典中的特定字段
fields_type = [
    ('Price', float),
    ('Change', float),
    ('Volume', int)
]
with open('p01.csv') as f:
    for row in csv.DictReader(f):
        # row.update((key, convert(row[key])) for key, convert in fields_type)
        # row.update({key: convert(row[key]) for key, convert in fields_type})
        row.update(**{key: convert(row[key]) for key, convert in fields_type})
        print(row)

# 可以pandas.read_csv()来读取csv数据 再进行数据分析和统计
