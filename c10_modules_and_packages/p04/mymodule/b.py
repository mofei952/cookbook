#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/12/8 16:05
# @File    : b.py
# @Software: PyCharm

from .a import A


class B(A):
    def bar(self):
        print('B.bar')
