#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/7/25 19:55
# @File    : p05_pack_unpack_large_int_from_bytes.py
# @Software: PyCharm

# 字节到大整数的打包与解包
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c03/p05_pack_unpack_large_int_from_bytes.html

# 使用 int.from_bytes() 方法将bytes解析为整数
data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
print(len(data))
print(int.from_bytes(data, 'little'))  # 指定字节顺序为little
print(int.from_bytes(data, 'big'))  # 指定字节顺序为big big代表使用大端存储 较高的有效字节存放在较低的存储器地址，较低的有效字节存放在较高的存储器地址。

# 使用 int.to_bytes() 方法将一个大整数转换为一个字节字符串
x = 94522842520747284487117727783387188
print(x.to_bytes(16, 'big'))
print(x.to_bytes(16, 'little'))

#  可以使用 int.bit_length() 方法来决定需要多少字节位来存储这个值。
x = 523 ** 23
print(x.bit_length())
nbytes, rem = divmod(x.bit_length(), 8)
if rem:
    nbytes += 1
print(x.to_bytes(nbytes, 'little'))
