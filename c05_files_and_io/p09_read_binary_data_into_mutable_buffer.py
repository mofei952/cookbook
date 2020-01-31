#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2020/1/16 21:31
# @File    : p09_read_binary_data_into_mutable_buffer.py
# @Software: PyCharm

"""读取二进制数据到可变缓冲区中"""

import os


# 为了读取数据到一个可变数组中，使用文件对象的 readinto() 方法
def read_into_buffer(filename):
    buf = bytearray(os.path.getsize(filename))
    with open(filename, 'rb') as f:
        f.readinto(buf)
    return buf


# 使用read_into_buffer的例子
with open('p09.bin', 'wb') as f:
    f.write(b'hello world')

buf = read_into_buffer('p09.bin')
print(buf)
buf[:5] = b'hhhhh'
print(buf)
with open('p09.bin', 'wb') as f:
    f.write(buf)

# readinto() 填充已存在的缓冲区而不是为新对象重新分配内存再返回它们。因此，可以使用它来避免大量的内存分配操作。
# 比如，如果读取一个由相同大小的记录组成的二进制文件时
with open('p09.bin', 'wb') as f:
    f.write(b'12345ABCDE12345AA')

record_size = 5
buf = bytearray(record_size)
with open('p09.bin', 'rb') as f:
    while True:
        n = f.readinto(buf)
        # 使用 f.readinto() 时需要注意的是，必须检查它的返回值，也就是实际读取的字节数。
        if n < record_size:
            print(buf[:n])
            break
        print(buf)

# memoryview可以通过零复制的方式对已存在的缓冲区执行切片操作，甚至还能修改它的内容
buf = bytearray(b'Hello World')
m1 = memoryview(buf)
m2 = m1[-5:]
print(m2)
m2[:] = b'WORLD'
print(buf)
