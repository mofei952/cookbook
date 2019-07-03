#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/7/3 19:35
# @File    : p06_search_replace_case_insensitive.py
# @Software: PyCharm

# 字符串忽略大小写的搜索替换
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c02/p06_search_replace_case_insensitive.html

# 为了在文本操作时忽略大小写，你需要在使用 re 模块的时候给这些操作提供 re.IGNORECASE 标志参数
import re
text = 'UPPER PYTHON, lower python, Mixed Python'
print(re.findall('python', text, flags=re.IGNORECASE))
print(re.sub('python', 'snake', text, flags=re.IGNORECASE))

# 替换字符串并不会自动跟被匹配字符串的大小写保持一致。这里可以需要一个辅助函数去实现
def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace
print(re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE))
