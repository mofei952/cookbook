#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/12/5 18:39
# @File    : spam.py
# @Software: PyCharm

import sys
print(sys.path)
# 相对导入
from . import grok
from ..B import bar

print(grok)
print(bar)

# 绝对导入
from p03.A import grok

print(grok)

