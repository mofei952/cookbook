#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2020/3/11 19:25
# @File    : p03_parse_simple_xml_data.py
# @Software: PyCharm

"""解析简单的XML数据"""

from urllib.request import urlopen
from xml.etree.ElementTree import parse

# 使用 xml.etree.ElementTree 模块从简单的XML文档中提取数据
u = urlopen('http://planet.python.org/rss20.xml')
doc = parse(u)

for item in doc.iterfind('channel/item'):
    title = item.findtext('title')
    date = item.findtext('pubDate')
    link = item.findtext('link')

    print(title)
    print(date)
    print(link)
    print()
