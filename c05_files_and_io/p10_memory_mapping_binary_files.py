#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2020/1/26 16:31
# @File    : p10_memory_mapping_binary_files.py
# @Software: PyCharm

"""内存映射的二进制文件"""

import os
import mmap


# 使用 mmap 模块来内存映射文件
def memory_map(filename, access=mmap.ACCESS_WRITE):
    size = os.path.getsize(filename)
    fd = os.open(filename, os.O_RDWR)
    return mmap.mmap(fd, size, access=access)


# 创建一个文件并将其内容扩充给的指定大小
size = 1000
with open('p10', 'wb') as f:
    f.seek(size - 1)
    f.write(b'\x00')

m = memory_map('p10')
print(len(m))
print(m[:10])
print(m[0])
m[:11] = b'Hello world'
m.close()

with open('p10', 'rb') as f:
    print(f.read(11))

# mmap()返回的mmap对象同样也可以作为上下文管理器来使用，这时候底层的文件会被自动关闭
with memory_map('p10') as m:
    print(len(m))
    print(m[:11])
print(m.closed)

# 默认情况下，memory_map()函数打开的文件同时支持读和写操作
# 如果需要只读的访问模式，可以给参数 access 赋值为 mmap.ACCESS_READ
m = memory_map('p10', mmap.ACCESS_READ)

# 如果想在本地修改数据，但是又不想将修改写回到原始文件中，可以使用 mmap.ACCESS_COPY
m = memory_map('p10', mmap.ACCESS_COPY)

# 为了随机访问文件的内容，使用 mmap 将文件映射到内存中是一个高效和优雅的方法。
# 例如，无需打开一个文件并执行大量的 seek() ， read() ， write() 调用， 只需要简单的映射文件并使用切片操作访问数据即可。

# 一般来讲， mmap() 所暴露的内存看上去就是一个二进制数组对象。 但是，可以使用一个内存视图来解析其中的数据
m = memory_map('p10')
# Memoryview of unsigned integers
v = memoryview(m).cast('I')
v[0] = 7
print(m[0:4])
m[0:4] = b'\x07\x01\x00\x00'
print(v[0])
