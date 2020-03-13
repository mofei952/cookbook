#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2020/3/13 20:46
# @File    : p06_parse_modify_rewrite_xml.py
# @Software: PyCharm

"""解析和修改XML"""

from xml.etree.ElementTree import parse, Element

# 获取节点的方式
doc = parse('p06.xml')
root = doc.getroot()
print(root)
print(root[0])
print(root[2:4])

# 移除节点
root.remove(root.find('sri'))
root.remove(root.find('cr'))

# 新增节点，可以使用insert或append
index = root.getchildren().index(root.find('nm'))
print(index)
e = Element('spam')
e.text = 'This is a text'
root.insert(index, e)

# 写入文件
doc.write('p06_2.xml')
