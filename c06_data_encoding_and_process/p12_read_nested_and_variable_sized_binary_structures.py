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
            f.write(struct.pack('<i', size))
            for pt in poly:
                f.write(struct.pack('<dd', *pt))


write_polys('p12.bin', polys)


# 从二进制文件中读取多边形数据
# 读取多边形数据时，先读取第一个位置的字节长度信息，再读取指定长度的数据
def read_polys(filename):
    with open(filename, 'rb') as f:
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
print()


# 使用类来解析字节数据
class StructField:
    def __init__(self, format, offset):
        self.format = format
        self.offset = offset

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            r = struct.unpack_from(self.format, instance._buffer, self.offset)
            return r[0] if len(r) == 1 else r


class Structure:
    def __init__(self, bytedata):
        self._buffer = memoryview(bytedata)


class PolyHeader(Structure):
    file_code = StructField('<i', 0)
    min_x = StructField('<d', 4)
    min_y = StructField('<d', 12)
    max_x = StructField('<d', 20)
    max_y = StructField('<d', 28)
    num_polys = StructField('<i', 36)


f = open('p12.bin', 'rb')
phead = PolyHeader(f.read(40))
print(phead.file_code == 0x1234)
print(phead.min_x)
print(phead.min_y)
print(phead.max_x)
print(phead.max_y)
print(phead.num_polys)
print()


# 使用元类改造Structure类
class StructureMeta(type):

    def __init__(self, clsname, bases, clsdict):
        fields = getattr(self, '_fields_', [])
        byte_order = ''
        offset = 0
        for format, fieldname in fields:
            if format.startswith(('<', '>', '!', '@')):
                byte_order = format[0]
                format = format[1:]
            format = byte_order + format
            setattr(self, fieldname, StructField(format, offset))
            offset += struct.calcsize(format)
        setattr(self, 'struct_size', offset)


class Structure(metaclass=StructureMeta):
    def __init__(self, bytedata):
        self._buffer = bytedata

    @classmethod
    def from_file(cls, f):
        return cls(f.read(cls.struct_size))


class PolyHeader(Structure):
    _fields_ = [
        ('<i', 'file_code'),
        ('d', 'min_x'),
        ('d', 'min_y'),
        ('d', 'max_x'),
        ('d', 'max_y'),
        ('i', 'num_polys')
    ]


f = open('p12.bin', 'rb')
phead = PolyHeader.from_file(f)
print(phead.file_code == 0x1234)
print(phead.min_x)
print(phead.min_y)
print(phead.max_x)
print(phead.max_y)
print(phead.num_polys)
print()


# 改进元类，支持嵌套字节结构
class NestedStruct:
    def __init__(self, name, struct_type, offset):
        self.name = name
        self.struct_type = struct_type
        self.offset = offset

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            data = instance._buffer[self.offset:self.offset + self.struct_type.struct_size]
            result = self.struct_type(data)
            setattr(instance, self.name, result)
            return result


class StructureMeta(type):
    def __init__(self, clsname, bases, clsdict):
        fields = getattr(self, '_fields_', [])
        byte_order = ''
        offset = 0
        for format, fieldname in fields:
            if isinstance(format, StructureMeta):
                setattr(self, fieldname, NestedStruct(fieldname, format, offset))
                offset += format.struct_size
            else:
                if format.startswith(('<', '>', '!', '@')):
                    byte_order = format[0]
                    format = format[1:]
                format = byte_order + format
                setattr(self, fieldname, StructField(format, offset))
                offset += struct.calcsize(format)
        setattr(self, 'struct_size', offset)


class Structure(metaclass=StructureMeta):
    def __init__(self, bytedata):
        self._buffer = bytedata

    @classmethod
    def from_file(cls, f):
        return cls(f.read(cls.struct_size))


class Point(Structure):
    _fields_ = [
        ('<d', 'x'),
        ('d', 'y')
    ]


class PolyHeader(Structure):
    _fields_ = [
        ('<i', 'file_code'),
        (Point, 'min'),  # nested struct
        (Point, 'max'),  # nested struct
        ('i', 'num_polys')
    ]


f = open('p12.bin', 'rb')
phead = PolyHeader.from_file(f)
print(phead.file_code == 0x1234)
print(phead.min.x)
print(phead.min.y)
print(phead.max.x)
print(phead.max.y)
print(phead.num_polys)
