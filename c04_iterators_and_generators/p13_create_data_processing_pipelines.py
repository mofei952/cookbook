#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/8/15 19:43
# @File    : p13_create_data_processing_pipelines.py
# @Software: PyCharm

# 创建数据处理管道
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c04/p13_create_data_processing_pipelines.html
import fnmatch
import os
import re


def gen_find(filepat, top):
    for root, dirs, files in os.walk(top):
        for file in fnmatch.filter(files, filepat):
            yield os.path.join(root, file)


def gen_opener(filenames):
    for filename in filenames:
        with open(filename) as f:
            yield f


def gen_concatenate(iterators):
    for it in iterators:
        yield from it


def gen_grep(pattern, lines):
    pat = re.compile(pattern)
    for line in lines:
        line = line.strip()
        if pat.search(line):
            yield line


logfilenames = gen_find('log*', 'p13')
logfiles = gen_opener(logfilenames)
lines = gen_concatenate(logfiles)
pylines = gen_grep('(?i)python', lines)
for line in pylines:
    print(line)

# 使用生成器表达式扩展通道
logfilenames = gen_find('log*', 'p13')
logfiles = gen_opener(logfilenames)
lines = gen_concatenate(logfiles)
pylines = gen_grep('(?i)python', lines)
countcolumn = (line.rsplit(None, 1)[1] for line in pylines)
counts = (int(x) for x in countcolumn if x != '-')
print(sum(counts))
print()


# 自定义的search方法
def search_file(filename, pattern):
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if not re.search(pattern, line):
                continue
            yield line


def search_files(top, filepat, pattern):
    filenames = gen_find(filepat, top)
    for filename in filenames:
        yield from search_file(filename, pattern)


for line in search_file('p13/log1.txt', '(?i)python'):
    print(line)
print()
for line in search_files('p13', 'log*', '(?i)python'):
    print(line)
