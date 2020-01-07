#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/8/15 19:43
# @File    : p13_create_data_processing_pipelines.py
# @Software: PyCharm

"""创建数据处理管道"""

import fnmatch
import os
import re


# 假定要处理一个非常大的日志文件目录，可以定义一个由多个执行特定任务独立任务的简单生成器函数组成的容器
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


# 将生成器函数连起来创建一个处理管道，比如查找包含单词python的所有日志行
logfilenames = gen_find('log*', 'p13')
logfiles = gen_opener(logfilenames)
lines = gen_concatenate(logfiles)
pylines = gen_grep('(?i)python', lines)
for line in pylines:
    print(line)
print()

# 之后可以再使用生成器表达式扩展通道，比如计算传输的字节数并计算其总和
logfilenames = gen_find('log*', 'p13')
logfiles = gen_opener(logfilenames)
lines = gen_concatenate(logfiles)
pylines = gen_grep('(?i)python', lines)
bytecolumn = (line.rsplit(None, 1)[1] for line in pylines)
bytes = (int(x) for x in bytecolumn if x != '-')
print(sum(bytes))
print()


# 自定义search_file方法，可以在指定文件中查找包含单词python的所有行
def search_file(filename, pattern):
    pat = re.compile(pattern)
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if pat.search(line):
                yield line


for line in search_file('p13/log1.txt', '(?i)python'):
    print(line)
print()


# search_files方法，可以查找目录中指定文件内容
def search_files(top, filepat, pattern):
    filenames = gen_find(filepat, top)
    for filename in filenames:
        yield from search_file(filename, pattern)


for line in search_files('p13', 'log*', '(?i)python'):
    print(line)
