#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/7/3 20:13
# @File    : p07_specify_regexp_for_shortest_match.py
# @Software: PyCharm

# 最短匹配模式
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c02/p07_specify_regexp_for_shortest_match.html

# 假如要匹配双引号包含的文本，可能返回的结果不是想要的
import re
str_pat = re.compile(r'"(.*)"')
text1 = 'Computer says "no."'
print(str_pat.findall(text1))
text2 = 'Computer says "no." Phone says "yes."'
print(str_pat.findall(text2))

# 在模式中的*操作符后面加上?修饰符，使得匹配变成非贪婪模式，从而得到最短的匹配
str_pat = re.compile(r'"(.*?)"')
text2 = 'Computer says "no." Phone says "yes."'
print(str_pat.findall(text2))

# 默认匹配模式为贪婪模式，可以通过在 * 或者 + 这样的操作符后面添加一个 ? 可以强制匹配算法改成寻找最短的可能匹配