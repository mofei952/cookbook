#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/9/1 17:20
# @File    : p09_replace_single_method_classes_with_functions.py
# @Software: PyCharm

# 将单方法的类转换为函数
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c07/p09_replace_single_method_classes_with_functions.html

# 可以使用闭包来将单个方法的类转换成函数
from urllib.request import urlopen

class UrlTemplate:
    def __init__(self, template):
        self.template = template

    def open(self, **kwargs):
        return urlopen(self.template.format_map(kwargs))

yahoo = UrlTemplate('http://finance.yahoo.com/d/quotes.csv?s={names}&f={fields}')
for line in yahoo.open(names='IBM,AAPL,FB', fields='sl1c1v'):
    print(line.decode('utf-8'))



def urltemplate(template):
    def opener(**kwargs):
        return urlopen(template.format_map(kwargs))
    return opener

yahoo = urltemplate('http://finance.yahoo.com/d/quotes.csv?s={names}&f={fields}')
for line in yahoo(names='IBM,AAPL,FB', fields='sl1c1v'):
    print(line.decode('utf-8'))
    

# 使用一个内部函数或者闭包的方案通常会更优雅一些
# 一个闭包就是一个函数， 只不过在函数内部带上了一个额外的变量环境
# 闭包关键特点就是它会记住自己被定义时的环境