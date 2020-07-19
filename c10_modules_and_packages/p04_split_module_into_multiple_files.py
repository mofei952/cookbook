#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/12/8 15:55
# @File    : p04_split_module_into_multiple_files.py
# @Software: PyCharm

""" 将模块分割为多个文件 """

from p04 import mymodule

a = mymodule.A()
a.spam()

b = mymodule.B()
b.bar()


# 延迟加载的主要缺点是继承和类型检查可能会中断
# print(isinstance(a, mymodule.A))  # TypeError: isinstance() arg 2 must be a type or tuple of types
print(isinstance(a, mymodule.a.A))
