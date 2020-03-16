#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2020/3/16 19:30
# @File    : p09_decode_encode_hexadecimal_digits.py
# @Software: PyCharm

"""编码和解码十六进制数"""

import base64
import binascii

# 使用binascii模块
s = b'hello'
h = binascii.b2a_hex(s)
print(h)
print(binascii.a2b_hex(h))

# 用base64模块实现同样的功能
h = base64.b16encode(s)
print(h)
print(base64.b16decode(h))

# 使用hex函数实现
h = s.hex()
print(h)
print(bytes.fromhex(h))
