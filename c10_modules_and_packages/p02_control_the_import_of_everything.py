#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/12/5 18:04
# @File    : p02_control_the_import_of_everything.py
# @Software: PyCharm

# from module import * 默认会导入所有不以下划线开头的
# 如果定义了 __all__ , 那么只有被列举出的东西会被导入
from c10_modules_and_packages.p02.test import *

print(spam)
print(grok)
# print(blah) # NameError: name 'blah' is not defined
