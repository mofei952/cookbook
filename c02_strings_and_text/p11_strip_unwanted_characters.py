#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/7/5 22:24
# @File    : p11_strip_unwanted_characters.py
# @Software: PyCharm

"""删除字符串中不需要的字符"""

import re

# strip() 方法能用于删除开始或结尾的字符。 lstrip() 和 rstrip() 分别从左和从右执行删除操作
# 默认情况下会去除空白字符，指定时去除指定字符
# Whitespace stripping
s = ' hello world \n'
print(s.strip())
print(s.lstrip())
print(s.rstrip())
# Character stripping
t = '-----hello====='
print(t.lstrip('-'))
print(t.strip('-='))

# 去除操作不会对字符串的中间的文本产生任何影响
s = ' hello     world \n'
s = s.strip()
print(s)

# 要去除字符串中间的空格，可以使用 replace() 方法或者是用正则表达式替换
print(s.replace(' ', ''))
print(re.sub('\s+', ' ', s))

# 通常情况下字符串 strip 操作和其他迭代操作相结合，比如从文件中读取多行数据。
with open('p11.txt') as f:
    lines = (line.strip() for line in f)
    for line in lines:
        print(line)

# 生成器表达式 lines = (line.strip() for line in f) 执行数据转换操作。
# 这种方式非常高效，因为它不需要预先读取所有数据放到一个临时的列表中去。
# 它仅仅只是创建一个生成器，并且每次返回行之前会先执行 strip 操作
