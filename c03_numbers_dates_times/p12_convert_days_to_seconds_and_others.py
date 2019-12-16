#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/8/1 20:05
# @File    : p12_convert_days_to_seconds_and_others.py
# @Software: PyCharm

"""基本的日期与时间转换"""

from datetime import timedelta, datetime
from dateutil.relativedelta import relativedelta, MO

# 使用 timedelta 实例来表示一个时间段，进行不同时间单位的转换和计算
a = timedelta(days=2, hours=6)
b = timedelta(hours=4.5)
c = a + b
print(c.days)
print(c.seconds)
print(c.seconds / 3600)
print(c.total_seconds())
print(c.total_seconds() / 3600)

# 使用datetime实例表示指定的日期和时间
a = datetime(2012, 9, 23)
print(a + timedelta(days=10))
b = datetime(2012, 12, 21)
d = b - a
print(d)
now = datetime.today()
print(now)
print(now + timedelta(minutes=10))

# datetime会自动处理闰年
a = datetime(2012, 3, 1)
b = datetime(2012, 2, 28)
print(a - b)
a = datetime(2013, 3, 1)
b = datetime(2013, 2, 28)
print(a - b)

# 可以使用 dateutil 模块来执行更加复杂的日期操作，比如处理时区，模糊时间范围，节假日计算等等
# 许多类似的时间计算可以使用 dateutil.relativedelta() 函数代替。它会在处理月份(还有它们的天数差距)的时候填充间隙
a = datetime(2012, 9, 23)
print(a)
# print(a+timedelta(months=1))# 'months' is an invalid keyword argument for this function
print(a + relativedelta(months=1))
print(a + relativedelta(months=4))
b = datetime(2012, 12, 21)
print(b - a)
d = relativedelta(b, a)
print(d.months)
print(d.days)
