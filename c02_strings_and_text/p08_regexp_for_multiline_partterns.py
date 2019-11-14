#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/7/3 21:18
# @File    : p08_regexp_for_multiline_partterns.py
# @Software: PyCharm

"""多行匹配模式"""

import re

# 跨越多行去匹配，注意(.)不能匹配换行符
comment = re.compile(r'/\*(.*?)\*/')
text1 = '/* this is a comment */'
text2 = '''/* this is a
multiline comment */
'''
print(comment.findall(text1))
print(comment.findall(text2))

# 增加对换行的支持
# (?:.|\n) 指定了一个非捕获组 (也就是它定义了一个仅仅用来做匹配，而不能通过单独捕获或者编号的组)。
comment = re.compile(r'/\*((?:.|\n)*?)\*/')
print(comment.findall(text2))

# re.compile() 函数接受一个标志参数叫 re.DOTALL
# 它可以让正则表达式中的点(.)匹配包括换行符在内的任意字符
comment = re.compile(r'/\*(.*?)\*/', re.DOTALL)
print(comment.findall(text2))
