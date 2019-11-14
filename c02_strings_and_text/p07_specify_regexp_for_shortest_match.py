#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/7/3 20:13
# @File    : p07_specify_regexp_for_shortest_match.py
# @Software: PyCharm

"""最短匹配模式"""

import re

# 假如要匹配双引号包含的文本，可能返回的结果不是想要的
str_pat = re.compile(r'"(.*)"')
text1 = 'Computer says "no."'
print(str_pat.findall(text1))
text2 = 'Computer says "no." Phone says "yes."'
print(str_pat.findall(text2))

# 在正则表达式中 * 表达式是贪婪的，因此匹配操作会查找最长的可能匹配
# 可以在 * 或者 + 这样的操作符后面添加一个 ? ，这样就使得匹配变成非贪婪模式，可以强制匹配算法改成寻找最短的可能匹配
str_pat = re.compile(r'"(.*?)"')
text2 = 'Computer says "no." Phone says "yes."'
print(str_pat.findall(text2))
