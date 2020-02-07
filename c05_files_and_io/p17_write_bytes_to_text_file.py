#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2020/2/7 21:12
# @File    : p17_write_bytes_to_text_file.py
# @Software: PyCharm

"""将字节写入文件文件"""

import sys

# 将字节数据直接写入文件的缓冲区即可
# sys.stdout.write(b'Hello\n')  # TypeError: write() argument must be str, not bytes
sys.stdout.buffer.write(b'Hello\n')
with open('p17.txt', 'w') as f:
    f.buffer.write(b'Hello\xc3\xb1')

# 类似的，能够通过读取文本文件的buffer属性还读取二进制数据
with open('p17.txt') as f:
    print(f.buffer.read())

# I/O系统以层级结果的形式构建而成。buffer属性指向对应的带缓冲的二进制处理层，访问它的话就会绕过文本处理层
