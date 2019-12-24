#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/8/6 21:15
# @File    : p16_manipulate_dates_involving_timezone.py
# @Software: PyCharm

# 结合时区的日期操作

from datetime import datetime, timedelta

import pytz
from pytz import timezone

d = datetime(2012, 12, 21, 9, 30)
print(d)

# 将日期对象本地化，下面示例表示一个芝加哥时间
central = timezone('US/Central')
loc_d = central.localize(d)
print(loc_d)

# 本地化之后，可用转化那位其他时区的时间，下面示例转换为班加罗尔对应的事件
bang_d = loc_d.astimezone(timezone('Asia/Kolkata'))
print(bang_d)

# 本地化时间进行计算时需要注意夏令时的转换
# 比如，在2013年，美国标准夏令时时间开始于本地时间3月13日凌晨2:00(在那时，时间向前跳过一小时)
d = datetime(2013, 3, 10, 1, 45)
loc_d = central.localize(d)
print(loc_d)
later = loc_d + timedelta(minutes=30)
print(later)

# 结果错误是因为它并没有考虑在本地时间中有一小时的跳跃。 为了修正这个错误，可以使用时区对象 normalize() 方法
print(central.normalize(loc_d + timedelta(minutes=30)))

# 处理本地化日期的通常策略是先将所有日期转换为UTC时间，并用它来执行所有的中间存储和操作
loc_d = datetime(2012, 12, 21, 9, 30)
utc_d = loc_d.astimezone(pytz.utc)
print(utc_d)

# 转换为UTC之后，就不用去担心跟夏令时相关的问题
# 因此，可以跟之前一样放心的执行常见的日期计算。
# 当想将输出变为本地时间的时候，使用合适的时区去转换下就行了
later_utc = utc_d + timedelta(minutes=30)
print(later_utc.astimezone(central))

# 可以使用ISO 3166国家代码作为关键字去查阅字典 pytz.country_timezones 来获取到对应的时区名
print(pytz.country_timezones['CN'])
print(later_utc.astimezone(timezone('Asia/Shanghai')))
