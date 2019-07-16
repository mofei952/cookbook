#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/7/16 19:08
# @File    : p17_handle_html_xml_in_text.py
# @Software: PyCharm

# 在字符串中处理html和xml
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c02/p17_handle_html_xml_in_text.html


# 使用html.escape()进行转义编码
s = 'Elements are written as "<tag>text</tag>".'
import html
print(s)
print(html.escape(s))
# Disable escaping of quotes
print(html.escape(s, quote=False))

# 处理ASCII文本时，要将非ASCII文本对应的编码实体嵌入进去，
# 可以给某些I/O函数传递参数 errors='xmlcharrefreplace' 来达到这个目的
s = 'Spicy Jalapeo'
print(s.encode('ascii', errors='xmlcharrefreplace'))

# 使用一个合适的HTML或者XML解析器
s = 'Spicy &quot;Jalape&#241;o&quot.'
print(html.unescape(s))
t = 'The prompt is &gt;&gt;&gt;'
from xml.sax.saxutils import unescape
print(unescape(t))

# 如果在处理HTML或XML文本时，可以使用某个解析模块比如 html.parse 或 xml.etree.ElementTree
# 解析模块已经自动处理了相关的替换细节
