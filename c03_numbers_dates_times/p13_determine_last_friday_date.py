#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/8/2 21:37
# @File    : p13_determine_last_friday_date.py
# @Software: PyCharm

"""计算最后一个周五的日期"""

# 查找星期中某一天最后出现的日期，比如星期五
from datetime import datetime, timedelta
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
            'Friday', 'Saturday', 'Sunday']
def get_previous_byday(dayname, start_date=None):
    if start_date is None:
        start_date = datetime.today()
    day_num = start_date.weekday()
    day_num_target = weekdays.index(dayname)
    days_ago = day_num - day_num_target
    if days_ago <= 0:
        days_ago += 7
    target_date = start_date - timedelta(days_ago)
    return target_date
for weekday in weekdays:
    print(weekday, get_previous_byday(weekday, datetime(2012, 8, 28)))

# 使用 dateutil 模块中的 relativedelta() 函数执行同样的计算
from dateutil.relativedelta import relativedelta
from dateutil.rrule import MO, TU, WE, TH, FR, SA, SU
d = datetime.now()
print(d)
print(d + relativedelta(weekday=TH))
print(d + relativedelta(weekday=TH(-1)))
