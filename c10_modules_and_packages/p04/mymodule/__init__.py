#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/12/8 16:06
# @File    : __init__.py
# @Software: PyCharm

# from .a import A
# from .b import B


# 延迟导入
def A():
    from .a import A
    return A()

def B():
    from .b import B
    return B()
