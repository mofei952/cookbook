#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/12/5 18:37
# @File    : p03_import_submodules_by_relative_names.py
# @Software: PyCharm

""" 使用相对路径名导入包中子模块 """

from p03.A import spam


# 导入同级的包，包中可以相对导入
# python c10_modules_and_packages\p03_import_submodules_by_relative_names.py

# 如果包的部分被作为脚本直接执行，那它们将不起作用
# python c10_modules_and_packages/p03/A/spam.py

# 使用Python的-m选项来执行先前的脚本，相对导入将会正确运行
# cd c10_modules_and_packages;python -m p03.A.spam
