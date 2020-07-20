#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/12/9 21:55
# @File    : p05_separate_directories_import_by_namespace.py
# @Software: PyCharm

""" 利用命名空间导入目录分散的代码 """


# 通过导入有相同子模块的目录到python模块路径，这样会创建特殊的包命名空间模块
import sys
sys.path.extend(['p05/foo-package', 'p05/bar-package'])

# 两个不同的包目录将合并在一起，并能够正常工作
from spam import blah
from spam import grok
print(blah)
print(grok)

# 包命名空间的关键是确保顶级目录中没有__init__.py文件来作为共同的命名空间
# 只读的目录列表副本被存储在其__path__变量中
import spam
print(spam.__path__)

# 一个包是否被作为一个包命名空间的主要方法是检查其__file__属性。如果没有，那包是个命名空间
# print(spam.__file__)  # AttributeError: module 'spam' has no attribute '__file__'
