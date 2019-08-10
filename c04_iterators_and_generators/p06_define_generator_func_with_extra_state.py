#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/8/10 21:30
# @File    : p06_define_generator_func_with_extra_state.py
# @Software: PyCharm

# 带有外部状态的生成器函数
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c04/p06_define_generator_func_with_extra_state.html

from collections import deque


# 在类的__iter__方法中定义生成器，可以定义各种属性和方法供用户使用
class linehistory:
    def __init__(self, lines, histlen=3):
        self.lines = lines
        self.history = deque(maxlen=histlen)

    def __iter__(self):
        for lineno, line in enumerate(self.lines, 1):
            self.history.append((lineno, line))
            yield line

    def clear(self):
        self.history.clear()


lines = linehistory(['a', 'b', 'c', 'd', 'e'])
for line in lines:
    if line == 'd':
        for lineno, line in lines.history:
            print('{}:{}'.format(lineno, line), end=' ')
