#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/11/19 21:50
# @File    : p18_tokenizing_text.py
# @Software: PyCharm

"""字符串令牌解析"""

import re
from collections import namedtuple

text = 'foo = 23 + 42 * 10'

# 将以上文本字符串令牌化
NAME = r'(?P<NAME>[a-zA-Z][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'
master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))


def generate_tokens(pat, text):
    Token = namedtuple('Token', ['type', 'value'])
    scanner = pat.scanner(text)
    for m in iter(scanner.match, None):
        yield Token(m.lastgroup, m.group())


for tok in generate_tokens(master_pat, text):
    print(tok)
print()

# 使用生成器表达式来过滤空白令牌
tokens = (tok for tok in generate_tokens(master_pat, text) if tok.type != 'WS')
for tok in tokens:
    print(tok)
print()

# 使用扫描方法时，要确认使用正则表达式指定了所有输入中可能出现的文本序列，如果有任何不可匹配的文本出现了，扫描就会直接停止。
NAME = r'(?P<NAME>[a-zA-Z][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
WS = r'(?P<WS>\s+)'
master_pat = re.compile('|'.join([NAME, NUM, WS]))
for tok in generate_tokens(master_pat, 'foo = 1'):
    print(tok)
print()

# re 模块会按照指定好的顺序去做匹配。 因此，如果一个模式恰好是另一个更长模式的子字符串，那么需要确定长模式写在前面
LT = r'(?P<LT><)'
LE = r'(?P<LE><=)'
EQ = r'(?P<EQ>=)'
master_pat = re.compile('|'.join([LE, LT, EQ]))  # Correct
for tok in generate_tokens(master_pat, '<='):
    print(tok)
print()

# 下面这种模式是错误的，因为它会将文本<=匹配为令牌LT紧跟着EQ，而不是单独的令牌LE
master_pat = re.compile('|'.join([LT, LE, EQ]))  # Incorrect
for tok in generate_tokens(master_pat, '<='):
    print(tok)
