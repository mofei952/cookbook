#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/11/12 21:36
# @File    : p02_match_text_at_start_end.py
# @Software: PyCharm

import os
import re
from os import listdir
from urllib.request import urlopen

# 字符串开头或结尾匹配

# 检查字符串开头或结尾的一个简单方法是使用 str.startswith() 或者是 str.endswith() 方法
filename = 'spam.txt'
print(filename.endswith('.txt'))  # True
print(filename.startswith('file:'))  # False
url = 'http://www.python.org'
print(url.startswith('http:'))  # True

# 如果想检查多种匹配可能，只需要将所有的匹配项放入到一个元组中去， 然后传给 startswith() 或者 endswith() 方法
filenames = os.listdir('.')
print(filenames)
print([name for name in filenames if name.endswith(('.c', '.h'))])
print(any(name.endswith('.py') for name in filenames))

# 另一个例子
def read_data(name):
    if name.startswith(('http:', 'https:', 'ftp:')):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()

# 这个方法中必须要输入一个元组作为参数。 如果恰巧有一个 list 或者 set 类型的选择项， 要确保传递参数前先调用 tuple() 将其转换为元组类型
choices = ['http:', 'ftp:']
url = 'http://www.python.org'
# print(url.startswith(choices))#startswith first arg must be str or a tuple of str, not list
print(url.startswith(tuple(choices)))  # True

# startswith() 和 endswith() 方法提供了一个非常方便的方式去做字符串开头和结尾的检查。
# 类似的操作也可以使用切片来实现，但是代码看起来没有那么优雅
filename = 'spam.txt'
print(filename[-4:] == '.txt')
url = 'http://www.python.org'
print(url[:5] == 'http:' or url[:6] == 'https:' or url[:4] == 'ftp:')

# 你可以能还想使用正则表达式去实现，这种方式也行得通，但是对于简单的匹配实在是有点小材大用了
url = 'http://www.python.org'
print(re.match('http:|https:|ftp:', url))

# 当和其他操作比如普通数据聚合相结合的时候 startswith() 和 endswith() 方法是很不错的。
# 比如，下面这个语句检查某个文件夹中是否存在指定的文件类型
if any(name.endswith(('.c', '.h')) for name in listdir('.')):
    pass
