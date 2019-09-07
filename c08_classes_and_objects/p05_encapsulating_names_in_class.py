#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/9/7 18:14
# @File    : p05_encapsulating_names_in_class.py
# @Software: PyCharm

# 在类中封装属性名
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c08/p05_encapsulating_names_in_class.html

# Python程序员不去依赖语言特性去封装数据，而是通过遵循一定的属性和方法命名规约来达到这个效果

# 第一个约定是任何以单下划线_开头的名字都应该是内部实现，代表非公共属性
class A:
    def __init__(self):
        self._internal = 0
        self.public = 1

    def public_method(self):
        pass

    def _internal_method(self):
        pass


# 双下划线定义的私有属性，这种属性通过继承是无法被覆盖的
# 在内部属性应该在子类中隐藏起来的时候考虑使用
class B:
    def __init__(self):
        self.__private = 0

    def __private_method(self):
        pass

    def public_method(self):
        pass


class C(B):
    def __init__(self):
        super().__init__()
        self.__private = 1

    def __private_method(self):
        pass


# 定义的变量名和某个保留关键字冲突，可以使用单下划线作为后缀
lambda_ = 2.0
