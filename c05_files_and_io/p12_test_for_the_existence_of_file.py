#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2020/2/2 18:22
# @File    : p12_test_for_the_existence_of_file.py
# @Software: PyCharm

"""测试文件是否存在"""

import os
import time

filename = 'p12_test_for_the_existence_of_file.py'

# 使用os.path模块来测试一个文件或目录是否存在
print(os.path.exists(filename))
print(os.path.exists('aa.py'))

# 进一步测试文件是什么类型的
print(os.path.isdir(filename))
print(os.path.isfile(filename))
print(os.path.islink(filename))

# realpath会先获取连接到的文件路径，再获取绝对路径
print(os.path.realpath(filename))

# 获取元数据（比如文件大小或修改日期）
print(os.path.getsize(filename))
print(os.path.getmtime(filename))
print(time.ctime(os.path.getmtime(filename)))

# 使用os.stat()获取文件的元数据
meta = os.stat(filename)
print(meta.st_size)
print(meta.st_mtime)
