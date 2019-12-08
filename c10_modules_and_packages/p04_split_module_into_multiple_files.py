#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/12/8 15:55
# @File    : p04_split_module_into_multiple_files.py
# @Software: PyCharm

from p04 import mymodule

a = mymodule.A()
a.spam()

b = mymodule.B()
b.bar()

