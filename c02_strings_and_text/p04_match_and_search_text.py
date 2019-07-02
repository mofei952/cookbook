#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/7/2 20:38
# @File    : p04_match_and_search_text.py
# @Software: PyCharm

# 字符串匹配和搜索
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c02/p04_match_and_search_text.html


# 如果要匹配的是字面字符串，那么通常只需要调用基本字符串方法就行， 比如 str.find() , str.endswith() , str.startswith()
text = 'yeah, but no, but yeah, but no, but yeah'
# Exact match
print(text == 'yeah')
# Match at start or end
print(text.startswith('yeah'))
print(text.endswith('no'))
# Search for the location of the first occurrence
print(text.find('no'))

# 对于复杂的匹配需要使用正则表达式和 re 模块
text1 = '11/27/2012'
text2 = 'Nov 27, 2012'
import re
# Simple matching: \d+ means match one or more digits
if re.match(r'\d+/\d+/\d+', text1):
    print('yes')
else:
    print('no')
if re.match(r'\d+/\d+/\d+', text2):
    print('yes')
else:
    print('no')

# 如果你想使用同一个模式去做多次匹配，你应该先将模式字符串预编译为模式对象。
# 如果做大量的匹配和搜索操作的话，最好先编译正则表达式，然后再重复使用它。
# 模块级别的函数会将最近编译过的模式缓存起来，因此并不会消耗太多的性能，
# 但是如果使用预编译模式的话，你将会减少查找和一些额外的处理损耗。
datepat = re.compile(r'\d+/\d+/\d+')
if datepat.match(text1):
    print('yes')
else:
    print('no')
if datepat.match(text2):
    print('yes')
else:
    print('no')

# match() 总是从字符串开始去匹配，如果你想查找字符串任意部分的模式出现位置， 使用 findall() 方法去代替
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print(datepat.findall(text))

# 在定义正则式的时候，通常会利用括号去捕获分组。比如：
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')

# 捕获分组可以使得后面的处理更加简单，因为可以分别将每个组的内容提取出来。比如：
m = datepat.match('11/27/2012')
print(m)
# Extract the contents of each group
print(m.group())
print(m.group(1))
print(m.group(2))
print(m.group(3))
print(m.groups())
month, day, year = m.groups()
# Find all matches (notice splitting into tuples)
print(text)
print(datepat.findall(text))
for month, day, year in datepat.findall(text):
    print('{}-{}-{}'.format(year, month, day))

# findall() 方法会搜索文本并以列表形式返回所有的匹配。 如果你想以迭代方式返回匹配，可以使用 finditer() 方法来代替，比如：
for m in datepat.finditer(text):
    print(m.groups())

# 当写正则式字符串的时候，相对普遍的做法是使用原始字符串比如 r'(\d+)/(\d+)/(\d+)' 。
# 这种字符串将不去解析反斜杠，这在正则表达式中是很有用的。 如果不这样做的话，则必须使用两个反斜杠，类似 '(\\d+)/(\\d+)/(\\d+)' 。