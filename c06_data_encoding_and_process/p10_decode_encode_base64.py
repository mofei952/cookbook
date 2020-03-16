#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2020/3/16 20:12
# @File    : p10_decode_encode_base64.py
# @Software: PyCharm

"""编码解码Base64数据"""

import base64

# 使用base64模块的b64encode()和b64decode()函数
import re
import string

s = b'hello'
a = base64.b64encode(s)
print(a)

print(base64.b64decode(a))
print()

# 手动实现base64算法
# 算法原理：https://blog.csdn.net/weixin_39471249/article/details/79585231
s = 'hello'

digits = []
for c in s:
    digits.append(ord(c))
print(digits)

binstr = ''
for d in digits:
    t = bin(d)[2:]
    while len(t) < 8:
        t = '0' + t
    binstr += t
print(binstr)

binlist = re.findall('.{1,6}', binstr)
print(binlist)

b64mapping = string.ascii_uppercase + string.ascii_lowercase + string.digits + '+' + '/'
res = ''
for b in binlist:
    while len(b) < 6:
        b += '0'
    b = int(b, 2)
    res += b64mapping[b]

remainder = len(s) % 3
if remainder == 1:
    res += '=='
elif remainder == 2:
    res += '='
print(res)
