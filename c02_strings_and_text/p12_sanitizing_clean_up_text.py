#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/7/7 11:54
# @File    : p12_sanitizing_clean_up_text.py
# @Software: PyCharm

"""审查清理文本字符串"""

import sys
import unicodedata

# 用translate清理空白字符
s = 'pýtĥöñ\fis\tawesome\r\n'
remap = {
    ord('\t'): ' ',
    ord('\f'): ' ',
    ord('\r'): None,
}
a = s.translate(remap)
print(a)

# 使用 unicodedata.normalize() 将原始输入标准化为分解形式字符。
# 再调用 translate 函数删除所有重音符
cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode)
                         if unicodedata.combining(chr(c)))
b = unicodedata.normalize('NFD', a)
print(b)
print(b.translate(cmb_chrs))

# 作为另一个例子，这里构造一个将所有Unicode数字字符映射到对应的ASCII字符上的表格：
digitmap = {c: ord('0') + unicodedata.digit(chr(c))
            for c in range(sys.maxunicode)
            if unicodedata.category(chr(c)) == 'Nd'}
print(digitmap)
print(len(digitmap))
# Arabic digits
x = '\u0661\u0662\u0663'
print(x.translate(digitmap))

# 另一种清理文本的技术涉及到I/O解码与编码函数。这里的思路是先对文本做一些初步的清理，
# 然后再结合 encode() 或者 decode() 操作来清除或修改它。
print(a)
b = unicodedata.normalize('NFD', a)
print(b.encode('ascii', 'ignore').decode('ascii'))
