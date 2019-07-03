#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/7/2 21:01
# @File    : p05_search_and_replace_text.py
# @Software: PyCharm

# 字符串搜索和替换
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c02/p05_search_and_replace_text.html

# 对于简单的字面模式，直接使用 str.replace() 方法即可
text = 'yeah, but no, but yeah, but no, but yeah'
print(text.replace('yeah', 'yep'))

# 对于复杂的模式，使用 re 模块中的 sub() 函数。
# 若要将形式为 11/27/2012 的日期字符串改成 2012-11-27 。
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
import re
print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text))

# 如果你打算用相同的模式做多次替换，考虑先编译它来提升性能。
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
print(datepat.sub(r'\3-\1-\2', text))

# 对于更加复杂的替换，可以传递一个替换回调函数来代替，比如：
from calendar import month_abbr
def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))
print(datepat.sub(change_date, text))

# 如果除了替换后的结果外，你还想知道有多少替换发生了，可以使用 re.subn() 来代替。比如：
newtext, n = datepat.subn(r'\3-\1-\2', text)
print(newtext, n)

