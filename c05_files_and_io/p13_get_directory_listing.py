#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2020/2/2 18:37
# @File    : p13_get_directory_listing.py
# @Software: PyCharm

"""获取文件夹中的文件列表"""

import glob
import os

from fnmatch import fnmatch

# 使用os.listdir()函数来获取某个目录中的文件列表
print(os.listdir('.'))

# 结合os.path库中的一些函数来过滤文件列表
names = [name for name in os.listdir('../') if os.path.isfile(os.path.join('../', name))]
print(names)
dirnames = [name for name in os.listdir('../') if os.path.isdir(os.path.join('../', name))]
print(dirnames)

# 可以使用字符串的startswith()和endswith()方法来过滤文件列表
pyfiles = [name for name in os.listdir('../') if name.endswith('py')]
print(pyfiles)

# 对于文件名的匹配，可以使用glob或fnmatch模块
pyfiles = glob.glob('../*.py')
print(pyfiles)
pyfiles = [name for name in os.listdir('../') if fnmatch(name, '*.py')]
print(pyfiles)
