#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2020/3/12 20:48
# @File    : p05_turning_dictionary_into_xml.py
# @Software: PyCharm

"""将字典转换为XML"""

from xml.etree.ElementTree import Element, tostring


# 使用 xml.etree.ElementTree 库将字典转换为XML
def dict_to_xml(tag, d):
    elem = Element(tag)
    for key, val in d.items():
        child = Element(key)
        child.text = val
        elem.append(child)
    return elem


s = {'name': 'GOOG', 'shares': '100', 'price': '490.1'}
e = dict_to_xml('stock', s)
print(e)
print(tostring(e))

# 给某个元素添加属性值
e.set('id', '1234')
print(tostring(e))
