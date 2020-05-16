#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2020/5/16 12:18
# @File    : p18test.py
# @Software: PyCharm

from xmlrpc.client import ServerProxy

proxy = ServerProxy("http://localhost:15000/")
print(proxy.add(1, 2))
