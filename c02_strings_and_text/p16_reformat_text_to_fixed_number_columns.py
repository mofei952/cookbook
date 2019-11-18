#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/7/15 19:38
# @File    : p16_reformat_text_to_fixed_number_columns.py
# @Software: PyCharm

"""以指定列宽格式化字符串"""

import textwrap

# 使用 textwrap 模块来格式化字符串的输出
s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
the eyes, not around the eyes, don't look around the eyes, \
look into my eyes, you're under."
print(textwrap.fill(s, 70))
print(textwrap.fill(s, 40))
print(textwrap.fill(s, 40, initial_indent='    '))
print(textwrap.fill(s, 40, subsequent_indent='    '))

# 如果希望输出自动匹配终端大小，可以使用os.get_terminal_size()获取获取终端的大小尺寸
# import os
# print(os.get_terminal_size().columns)
