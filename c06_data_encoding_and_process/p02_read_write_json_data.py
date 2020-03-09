#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2020/3/9 19:44
# @File    : p02_read_write_json_data.py
# @Software: PyCharm

"""
读写JSON数据

json模块提供了一种很简单的方式来编码和解码JSON数据，其中两个主要的函数是json.dump()和json.loads()
"""

import json

from collections import OrderedDict
from pprint import pprint

# 将一个Python数据结构转换为JSON
data = {
    'name': 'ACME',
    'shares': 100,
    'prices': 542.23
}
json_str = json.dumps(data)
print(json_str)

# 将一个JSON编码的字符串转换回一个Python数据结构
data = json.loads(json_str)
print(data)

# 如果要处理文件，可用使用json.dump()和json.load()
with open('p02.json', 'w') as f:
    json.dump(data, f)

with open('p02.json', 'r') as f:
    data = json.load(f)
    print(data)

# json编码支持的基本数据类型为None, bool, int, float, str, 以及包含这些类型数据的lists，tuples和dictionaries。
# 对于dictionaries，keys需要是字符串类型（字典中任何非字符串类型的key在编码时会先转换为字符串）。
print(json.dumps({1: 'a', 2: ['b', 'c']}))

# json编码的格式对于Python语法而言几乎是完全一样的，除了一些小的差异之外。
# 比如，True会被映射为true，False会被映射为false，而None会被映射为null。
print(json.dumps(False))
print(json.dumps({'a': True, 'b': 'Hello', 'c': None}))

# 使用pprint()函数来打印，它会按照key的字母顺序并以一种更加美观的方式输出
with open('p02_2.json', 'r') as f:
    data = json.load(f)
pprint(data)

# 一般来讲，JSON解码会根据提供的数据创建dicts或lists
# 如果要创建其他类型的对象，可用给json.loads()传递object_pairs_hook或object_hook参数
s = '{"name": "ACME", "shares": 50, "price": 490.1}'
data = json.loads(s, object_pairs_hook=OrderedDict)
print(data)


# 将jSON字典转换为一个Python对象
class JSONObject:
    def __init__(self, d):
        self.__dict__ = d


obj = json.loads(s, object_hook=JSONObject)
print(obj.name)
print(obj.shares)

#  如果要获得漂亮的格式化字符串后输出，可以使用 json.dumps() 的indent参数
print(json.dumps(data))
print(json.dumps(data, indent=4))


# JSON序列化一个对象实例
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point({!r},{!r})'.format(self.x, self.y)


def serialize_instance(obj):
    d = {'__classname__': type(obj).__name__}
    d.update(vars(obj))
    return d


classes = {
    'Point': Point
}


def unserialize_object(d):
    clsname = d.pop('__classname__', None)
    if clsname:
        cls = classes[clsname]
        obj = cls.__new__(cls)
        for key, value in d.items():
            setattr(obj, key, value)
        return obj
    else:
        return d


p = Point(2, 3)
s = json.dumps(p, default=serialize_instance)
p = json.loads(s, object_hook=unserialize_object)
print(s)
print(p)
