#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2020/3/18 19:39
# @File    : p11_read_write_binary_arrays_of_structures.py
# @Software: PyCharm

"""读写二进制数组数据"""

from collections import namedtuple
from struct import Struct
import numpy as np


# 将元组写入二进制文件
def write_records(records, format, f):
    record_struct = Struct(format)
    for r in records:
        s = record_struct.pack(*r)
        print(s)
        f.write(s)


records = [
    (1, 2.3, 4.5),
    (6, 7.8, 9.0),
    (12, 13.4, 56.7)
]
with open('p11.b', 'wb') as f:
    write_records(records, '<idd', f)


# 读取文件并返回元组列表，以增量方式读取
def read_records(format, f):
    record_struct = Struct(format)
    chunks = iter(lambda: f.read(record_struct.size), b'')
    return (record_struct.unpack(chunk) for chunk in chunks)


with open('p11.b', 'rb') as f:
    for rec in read_records('<idd', f):
        print(rec)


# 先将整个文件内容一次性读到一个字节字符串中，然后再分片解析
def unpack_records(format, data):
    record_struct = Struct(format)
    return (record_struct.unpack_from(data, offset)
            for offset in range(0, len(data), record_struct.size))


with open('p11.b', 'rb') as f:
    data = f.read()
for rec in unpack_records('<idd', data):
    print(rec)

# 解包时，可以使用collections模块的命名元组对象
Records = namedtuple('Records', ['kind', 'x', 'y'])

with open('p11.b', 'rb') as f:
    records = [Records(*r) for r in read_records('<idd', f)]

for r in records:
    print(r, r.kind, r.x, r.y)

# 如果要处理大量的二进制数据，最好使用numpy模块
f = open('p11.b', 'rb')
records = np.fromfile(f, dtype='<i,<d,<d')
print(records)
print(records[0])
