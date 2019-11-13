#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/7/2 21:01
# @File    : p05_search_and_replace_text.py
# @Software: PyCharm

"""字符串搜索和替换"""

import calendar
import re
from calendar import month_abbr

# 对于简单的字面模式，直接使用 str.replace() 方法即可
text = 'yeah, but no, but yeah, but no, but yeah'
print(text.replace('yeah', 'yep'))

# 对于复杂的模式，使用 re 模块中的 sub() 函数
# 假设要将形式为 11/27/2012 的日期字符串改成 2012-11-27
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text))

# 如果打算用相同的模式做多次替换，考虑先编译它来提升性能。
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
print(datepat.sub(r'\3-\1-\2', text))


# 对于更加复杂的替换，可以传递一个替换回调函数来代替，比如：
def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))
print(datepat.sub(change_date, text))

# 使用 re.subn() 可以知道替换次数
newtext, n = datepat.subn(r'\3-\1-\2', text)
print(newtext, n)

# calendar的其他方法
print(calendar.firstweekday())  # 一周第一天默认为周一
print(calendar.weekheader(4))
print(calendar.monthcalendar(2019, 8))
print(calendar.month(2019, 7, w=0, l=0))
print(calendar.calendar(2019, w=2, l=1, c=6, m=4))
