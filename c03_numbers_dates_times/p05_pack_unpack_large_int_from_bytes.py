#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/7/25 19:55
# @File    : p05_pack_unpack_large_int_from_bytes.py
# @Software: PyCharm

"""字节到大整数的打包与解包"""

import struct

# 使用 int.from_bytes() 方法将bytes解析为整数
data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
print(len(data))
print(int.from_bytes(data, 'little'))  # 指定字节顺序为little
print(int.from_bytes(data, 'big'))  # 指定字节顺序为big

# 使用 int.to_bytes() 方法将一个大整数转换为一个字节字符串
x = 94522842520747284487117727783387188
print(x.to_bytes(16, 'big'))
print(x.to_bytes(16, 'little'))

# 使用struct模块来解压字节
hi, lo = struct.unpack('>QQ', data)
print((hi << 64) + lo)

# 字节顺序规则（little或big）仅仅指定了构造正数时的字节的低位高位排列方式
# big代表使用大端存储 较高的有效字节存放在较低的存储器地址，较低的有效字节存放在较高的存储器地址。
x = 0x01020304
print(x.to_bytes(4, 'big'))
print(x.to_bytes(4, 'little'))

# 如果不确定需要多少字节，可以使用 int.bit_length() 方法来决定需要多少字节位来存储这个值。
x = 523 ** 23
# x.to_bytes(16, 'little')  # OverflowError: int too big to convert
nbytes, rem = divmod(x.bit_length(), 8)
print(nbytes, rem)
if rem:
    nbytes += 1
print(x.to_bytes(nbytes, 'little'))
