#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2020/1/16 20:53
# @File    : p07_read_write_compressed_datafiles.py
# @Software: PyCharm

"""读写压缩文件"""

import gzip
import bz2

text = b'aaaaaaaaaaaaaaaaaa'

# 读写一个gzip或bz2格式的压缩文件
with gzip.open('p07.gz', 'wb') as f:
    f.write(text)

with gzip.open('p07.gz', 'rb') as f:
    text = f.read()
    print(text)

# 读写一个gzip或bz2格式的压缩文件
with bz2.open('p07.bz2', 'wb') as f:
    f.write(text)

with bz2.open('p07.bz2', 'rb') as f:
    text = f.read()
    print(text)

# gzip和bz2的open方法使用compresslevel这个可选的关键字参数来指定一个压缩级别
# 默认的等级是9，也是最高的压缩等级。等级越低性能越好，但是数据压缩程度也越低。
with gzip.open('p07.gz', 'wb', compresslevel=5) as f:
    f.write(text)

with gzip.open('p07.gz', 'rb') as f:
    text = f.read()
    print(text)

# gzip.open() 和 bz2.open() 还可以作用在一个已存在并以二进制模式打开的文件上。
f = open('p07.gz', 'rb')
with gzip.open(f, 'rb') as g:
    text = g.read()
    print(text)
