#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2020/3/20 22:04
# @File    : p12_read_nested_and_variable_sized_binary_structures.py
# @Software: PyCharm

"""读取嵌套和可变长二进制数据"""

import struct
import itertools

# 下面的数据结果表示一系列多边形，每个多边形由多个坐标点组成
polys = [
    [(1.0, 2.5), (3.5, 4.0), (2.5, 1.5)],
    [(7.0, 1.2), (5.1, 3.0), (0.5, 7.5), (0.8, 9.0)],
    [(3.4, 6.3), (1.2, 0.5), (4.6, 9.2)],
]


# 以下代码是将上面的数据写入到二进制文件
# 文件头部是固定长度的多边形汇总信息
# 然后写入多边形数据，每个多边形数据写入前会先写入字节长度，方便读取时使用
def write_polys(filename, polys):
    # Determine bounding box
    flattened = list(itertools.chain(*polys))
    min_x = min(x for x, y in flattened)
    max_x = max(x for x, y in flattened)
    min_y = min(y for x, y in flattened)
    max_y = max(y for x, y in flattened)
    with open(filename, 'wb') as f:
        f.write(struct.pack('<iddddi', 0x1234,
                            min_x, min_y,
                            max_x, max_y,
                            len(polys)))
        for poly in polys:
            size = len(poly) * struct.calcsize('<dd')
            f.write(struct.pack('<i', size + 4))
            for pt in poly:
                f.write(struct.pack('<dd', *pt))


write_polys('p12.bin', polys)


# 从二进制文件中读取多边形数据
# 读取多边形数据时，先读取第一个位置的字节长度信息，再读取指定长度的数据
def read_polys(filename):
    with open(filename, 'rb') as f:
        # Read the header
        header = f.read(40)
        file_code, min_x, min_y, max_x, max_y, num_polys = \
            struct.unpack('<iddddi', header)
        polys = []
        for n in range(num_polys):
            pbytes, = struct.unpack('<i', f.read(4))
            poly = []
            for m in range(pbytes // 16):
                pt = struct.unpack('<dd', f.read(16))
                poly.append(pt)
            polys.append(poly)
    return polys


polys = read_polys('p12.bin')
for poly in polys:
    print(poly)
