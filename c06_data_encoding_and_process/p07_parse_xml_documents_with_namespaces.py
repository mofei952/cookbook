#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2020/3/13 21:00
# @File    : p07_parse_xml_documents_with_namespaces.py
# @Software: PyCharm

"""利用命名空间解析XML文档"""
from functools import partial
from xml.etree.ElementTree import parse, iterparse

# 解析带有命名空间的XML会非常繁琐
doc = parse('p07.xml')
print(doc.find('content'))

print(doc.find('content/html'))  # None
print(doc.find('content/{http://www.w3.org/1999/xhtml}html'))

print(doc.findtext('content/{http://www.w3.org/1999/xhtml}html/head/title'))  # None
print(doc.findtext(
    'content/{http://www.w3.org/1999/xhtml}html/{http://www.w3.org/1999/xhtml}head/{http://www.w3.org/1999/xhtml}title'))
print()


# 将命名空间处理逻辑包装成一个工具类来简化这个过程
class XMLNamespaces:
    def __init__(self, **kwargs):
        self.namespaces = {}
        for name, uri in kwargs.items():
            self.register(name, uri)

    def register(self, name, uri):
        self.namespaces[name] = '{' + uri + '}'

    def __call__(self, path):
        return path.format_map(self.namespaces)


ns = XMLNamespaces(html='http://www.w3.org/1999/xhtml')
print(doc.find(ns('content/{html}html')))
print(doc.findtext(ns('content/{html}html/{html}head/{html}title')))
print()


# 使用偏函数也可以进行简化
def ns(s, **kwargs):
    namespaces = {k: '{' + v + '}' for k, v in kwargs.items()}
    return s.format_map(namespaces)


ns = partial(ns, html='http://www.w3.org/1999/xhtml')
print(doc.find(ns('content/{html}html')))
print()

# 使用iterparse()可以获取更多关于命名空间处理范围的信息
for evt, elem in iterparse('p07.xml', ('end', 'start-ns', 'end-ns')):
    print(evt, elem)
