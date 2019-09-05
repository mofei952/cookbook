#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/9/5 23:23
# @File    : p02_customizing_string_formatting.py
# @Software: PyCharm

# 自定义字符串的格式化
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c08/p02_customizing_string_formatting.html

_formats = {
    'ymd': '{d.year}-{d.month}-{d.day}',
    'mdy': '{d.month}/{d.day}/{d.year}',
    'dmy': '{d.day}/{d.month}/{d.year}'
}


# 在类上面定义 __format__() 方法
class Date():
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __format__(self, code):
        if code == '':
            code = 'ymd'
        fmt = _formats[code]
        return fmt.format(d=self)


d = Date(2012, 12, 21)
print(format(d))
print(format(d, 'mdy'))
print('The date is {:ymd}'.format(d))
print('The date is {:mdy}'.format(d))
