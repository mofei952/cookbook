#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/12/5 18:05
# @File    : test.py
# @Software: PyCharm

def spam():
    pass


def grok():
    pass


blah = 42

# Only export 'spam' and 'grok'
__all__ = ['spam', 'grok']
