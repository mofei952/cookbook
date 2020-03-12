#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2020/3/11 21:21
# @File    : p04_parse_huge_xml_files_incrementally.py
# @Software: PyCharm

from collections import Counter
from xml.etree.ElementTree import iterparse, parse

from memory_profiler import profile


# 使用parse
@profile
def test1():
    potholes_by_zip = Counter()

    doc = parse('p04.xml')
    for pothole in doc.iterfind('rows/row'):
        potholes_by_zip[pothole.findtext('zip')] += 1
    for zipcode, num in potholes_by_zip.most_common():
        print(zipcode, num)


test1()


# 如果XML数据很大，超过了100000行
# 那么使用如下代码比上面的代码，可以大大节约内存资源，但运行速度可能没有那么快
def parse_and_remove(filename, path):
    path_parts = path.split('/')
    doc = iterparse(filename, ('start', 'end'))
    # Skip the root element
    next(doc)

    tag_stack = []
    elem_stack = []
    for event, elem in doc:
        if event == 'start':
            tag_stack.append(elem.tag)
            elem_stack.append(elem)
        elif event == 'end':
            if tag_stack == path_parts:
                yield elem
                elem_stack[-2].remove(elem)
            try:
                tag_stack.pop()
                elem_stack.pop()
            except IndexError:
                pass


@profile
def test2():
    potholes_by_zip = Counter()

    data = parse_and_remove('p04.xml', 'rows/row')
    for pothole in data:
        potholes_by_zip[pothole.findtext('zip')] += 1
    for zipcode, num in potholes_by_zip.most_common():
        print(zipcode, num)


test2()
