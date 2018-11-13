#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/11/12 21:29
# @File    : p01_split_string_on_multiple_delimiters.py
# @Software: PyCharm

import re

# 使用多个界定符分割字符串

# string 对象的 split() 方法只适应于非常简单的字符串分割情形， 它并不允许有多个分隔符或者是分隔符周围不确定的空格。
# 当需要更加灵活的切割字符串的时候，最好使用re.split() 方法
line = 'asdf fjdk; afed, fjek,asdf, foo'
print(re.split(r'[;,\s]\s*', line))  # ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']

# 当使用re.split()函数时候，需要特别注意的是正则表达式中是否包含一个括号捕获分组。
# 如果使用了捕获分组，那么被匹配的文本也将出现在结果列表中。
fields = re.split(r'(;|,|\s)\s*', line)
print(fields)  # ['asdf', ' ', 'fjdk', ';', 'afed', ',', 'fjek', ',', 'asdf', ',', 'foo']

# 获取分割字符在某些情况下也是有用的。 比如, 保留分割字符串用来在后面重新构造一个新的输出字符串
values = fields[::2]
delimiters = fields[1::2] + ['']
print(values)  # ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']
print(delimiters)  # [' ', ';', ',', ',', ',', '']
print(''.join(v + d for v, d in zip(values, delimiters)))  # asdf fjdk;afed,fjek,asdf,foo

# 如果你不想保留分割字符串到结果列表中去，但仍然需要使用到括号来分组正则表达式的话， 确保你的分组是非捕获分组，形如 (?:...)
print(re.split(r'(?:,|;|\s)\s*', line))
