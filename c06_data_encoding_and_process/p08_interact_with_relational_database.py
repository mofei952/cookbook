#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2020/3/15 13:57
# @File    : p08_interact_with_relational_database.py
# @Software: PyCharm

"""与关系型数据库的交互"""

import os
import sqlite3

# 使用 sqlite3 来演示，第一步是连接到数据库
db = sqlite3.connect('p07db.db')

# 创建一个游标，然后就可以执行sql语句了
c = db.cursor()
c.execute('create table portfolio (symbol text, shares integer, price real)')
db.commit()

# 向数据库中插入多条记录
stocks = [
    ('GOOG', 100, 490.1),
    ('AAPL', 50, 545.75),
    ('FB', 150, 7.45),
    ('HPQ', 75, 33.2),
]
c.executemany('insert into portfolio values (?, ?, ?)', stocks)
db.commit()

# 执行查询
for row in db.execute('select * from portfolio'):
    print(row)
print()

# 使用占位符方式查询
min_price = 100
for row in db.execute('select * from portfolio where price >= ?', (min_price,)):
    print(row)

db.close()
os.remove('p07db.db')
