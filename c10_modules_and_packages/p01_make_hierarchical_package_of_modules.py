#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/11/14 21:28
# @File    : p01_make_hierarchical_package_of_modules.py
# @Software: PyCharm

"""构建一个模块的层级包"""

# 导入指定模块
from c10_modules_and_packages.p01 import jpg
import c10_modules_and_packages.p01.jpg as j

print(jpg)
print(j)

# 导入层级包，有有__init__文件才能导入
# 要访问指定模块必须在__init__文件中包含对应模块
from c10_modules_and_packages import p01

print(p01)
print(p01.jpg)
print(p01.png)

# 导入包中的所有模块
# 要将使用的模块在__init__文件中导入
from c10_modules_and_packages.p01 import *

print(jpg)
print(png)
