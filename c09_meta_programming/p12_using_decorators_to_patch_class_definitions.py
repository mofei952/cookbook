#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/10/29 21:11
# @File    : p12_using_decorators_to_patch_class_definitions.py
# @Software: PyCharm

"""使用装饰器扩充类的功能"""


# 使用类装饰器重写__getattribute__方法，用来打印日志
def log_getattribute(cls):
    orig_getattribute = cls.__getattribute__

    def new_getattribute(self, name):
        print('getting:', name)
        return orig_getattribute(self, name)

    cls.__getattribute__ = new_getattribute
    return cls


@log_getattribute
class A:
    def __init__(self, x):
        self.x = x

    def spam(self):
        pass


a = A(1)
print(a.x)
a.spam()
