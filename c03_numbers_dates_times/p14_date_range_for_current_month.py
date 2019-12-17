#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/8/3 19:47
# @File    : p14_date_range_for_current_month.py
# @Software: PyCharm

"""计算当前月份的日期范围"""

import calendar
from datetime import date, timedelta, datetime


# 先计算出开始日期和结束日期
def get_month_range(start_date=None):
    if start_date is None:
        start_date = date.today()
    _, days = calendar.monthrange(start_date.year, start_date.month)
    start_date = start_date.replace(day=1)
    end_date = start_date + timedelta(days=days)
    return start_date, end_date


# 使用 datetime.timedelta 递增日期变量
start_date, end_date = get_month_range()
a_day = timedelta(days=1)
temp_date = start_date
while temp_date < end_date:
    print(temp_date)
    temp_date += a_day


# 使用生成器实现简单的日期迭代，类似于内置的range函数
def date_range(start, end, step):
    while start < end:
        yield start
        start += step
for date_ in date_range(datetime(2019, 8, 1), datetime(2019, 8, 5), timedelta(hours=6)):
    print(date_)


# 结合以上两个内容
for date_ in date_range(*get_month_range(), timedelta(days=3)):
    print(date_)
