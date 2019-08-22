#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/8/22 22:14
# @File    : p04_read_write_binary_data.py
# @Software: PyCharm

# 读写字节数据
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c05/p04_read_write_binary_data.html

# 使用模式为 rb 或 wb 的 open() 函数来读取或写入二进制数据
with open('p04.bin', 'wb') as f:
    f.write(b'hello')

with open('p04.bin', 'rb') as f:
    print(f.read())

# 关于字节字符串，需要注意的是，索引和迭代动作返回的是字节的值而不是字节字符串
for c in b'hello':
    print(c)

# 从二进制模式的文件中读取或写入文本数据，必须确保要进行解码和编码操作
with open('p04.bin', 'wb') as f:
    text = 'world'
    f.write(text.encode('utf8'))

with open('p04.bin', 'rb') as f:
    data = f.read()
    print(data.decode('utf8'))

# 二进制I/O还有一个特性就是数组和C结构体类型能直接被写入，而不需要中间转换为自己对象
import array
nums = array.array('i', [1, 2, 3, 4])
with open('p04.bin', 'wb') as f:
    f.write(nums)

# 通过使用文件对象的 readinto() 方法直接读取二进制数据到其底层的内存中去
a = array.array('i', [0, 0, 0, 0, 0, 0, 0, 0])
with open('p04.bin', 'rb') as f:
    f.readinto(a)
print(a)
