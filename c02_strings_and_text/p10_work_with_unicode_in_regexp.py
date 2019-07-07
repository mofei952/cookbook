#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/7/5 22:06
# @File    : p10_work_with_unicode_in_regexp.py
# @Software: PyCharm

# 在正则式中使用Unicode
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c02/p10_work_with_unicode_in_regexp.html

# 默认情况下 re 模块已经对一些Unicode字符类有了基本的支持。 比如， \\d 已经匹配任意的unicode数字字符了
import re
num = re.compile('\d+')
# ASCII digits
print(num.match('123'))
# Arabic digits
print(num.match('\u0661\u0662\u0663'))

# 如果你想在模式中包含指定的Unicode字符，你可以使用Unicode字符对应的转义序列(比如 \uFFF 或者 \UFFFFFFF )。
# 比如，下面是一个匹配几个不同阿拉伯编码页面中所有字符的正则表达式：
arabic = re.compile('[\u0600-\u06ff\u0750-\u077f\u08a0-\u08ff]+')

# 当执行匹配和搜索操作的时候，最好是先标准化并且清理所有文本为标准化格式
# 但是同样也应该注意一些特殊情况，比如在忽略大小写匹配和大小写转换时的行为
pat = re.compile('stra\u00dfe', re.IGNORECASE)
s = 'straße'
print(pat.match(s)) # Matches
print(pat.match(s.upper())) # Doesn't match
print(s.upper()) # Case folds

# 混合使用Unicode和正则表达式通常会让你抓狂。
# 如果你真的打算这样做的话，最好考虑下安装第三方正则式库， 它们会为Unicode的大小写转换和其他大量有趣特性提供全面的支持，包括模糊匹配。