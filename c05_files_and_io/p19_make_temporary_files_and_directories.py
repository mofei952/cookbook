#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2020/3/3 18:58
# @File    : p19_make_temporary_files_and_directories.py
# @Software: PyCharm

"""创建临时文件和文件夹"""
import tempfile
from tempfile import TemporaryFile, NamedTemporaryFile, TemporaryDirectory

# 使用tempfile.TemporaryFile来创建临时文件
# TemporaryFile() 的第一个参数是文件模式，通常来讲文本模式使用 w+t ，二进制模式使用 w+b 。
with TemporaryFile('w+t') as f:
    # Read/write to the file
    f.write('Hello World\n')
    f.write('Testing\n')

    # Seek back to beginning and read the data
    f.seek(0)
    data = f.read()
    print(data)

# TemporaryFile() 另外还支持跟内置的 open() 函数一样的参数。
with TemporaryFile('w+t', encoding='utf-8') as f:
    pass

# 在大多数Unix系统上，通过 TemporaryFile() 创建的文件都是匿名的，甚至连目录都没有。
# 如果想打破这个限制，可以使用 NamedTemporaryFile() 来代替
with NamedTemporaryFile('w+t') as f:
    print('filename is:', f.name)

# 和 TemporaryFile() 一样，结果文件关闭时会被自动删除掉。
# 如果不想这么做，可以传递一个关键字参数 delete=False 即可
with NamedTemporaryFile('w+t', delete=False) as f:
    print('filename is:', f.name)

# 使用 tempfile.TemporaryDirectory() 创建一个目录
with TemporaryDirectory() as dirname:
    print('dirname is:', dirname)

# 在一个更低的级别，你可以使用 mkstemp() 和 mkdtemp() 来创建临时文件和目录
print(tempfile.mkstemp())
print(tempfile.mkdtemp())

# 使用 tempfile.gettempdir() 函数获取临时文件的默认位置
print(tempfile.gettempdir())
