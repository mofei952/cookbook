#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/8/5 20:02
# @File    : p15_convert_strings_into_datetimes.py
# @Software: PyCharm

# 字符串转换为日期
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c03/p15_convert_strings_into_datetimes.html

# 解析日期
from datetime import datetime
text = '2019-08-03'
y = datetime.strptime(text, '%Y-%m-%d')
z = datetime.now()
print(z - y)

# 日期格式化
nice_z = datetime.strftime(z, '%A %B %d, %Y')
print(nice_z)

# strptime() 的性能比较差，若要解析大量的日期，可以自己实现一个解析函数