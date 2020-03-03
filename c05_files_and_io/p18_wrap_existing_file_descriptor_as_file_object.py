#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2020/2/20 20:55
# @File    : p18_wrap_existing_file_descriptor_as_file_object.py
# @Software: PyCharm

"""将文件描述符包装成文件对象"""

import os
import sys
from socket import socket, AF_INET, SOCK_STREAM

# 在有对应于操作系统上一个已打开的I/O通道（比如文件、管道、套接字等）的整数文件描述符的情况下，可以将它包装成一个更高级的Python文件对象
# 一个文件描述符和一个打开的普通文件是不一样的。文件描述符仅仅是一个由操作系统指定的整数，用来指代某个系统的I/O通道。

# 可以通过使用open()函数来将其包装为一个Python的文件对象
fd = os.open('p18.txt', os.O_WRONLY | os.O_CREAT)
f = open(fd, 'w')
f.write('hello world\n')
f.close()

# 当高层的文件对象被关闭或者被破坏的时候，底层的文件描述符也会被关闭。
# 如果不想这样，可以给open()函数传递一个可选的closefd=False
fd = os.open('p18.txt', os.O_WRONLY | os.O_CREAT)
f = open(fd, 'w', closefd=False)
f.write('hello world\n')
f.close()
f = open(fd, 'w')
f.write('hello world\n')
f.close()


# 在unix系统中，这种包装文件描述符的技术可以很方便的将一个类文件接口作用于一个以不同方式打开的I/O通道上，如管道，套接字等
# 下面是一个操作管道的例子
def echo_client(client_sock, addr):
    print('Got connection from', addr)

    # Make text-mode file wrappers for socket reading/writing
    client_in = open(client_sock.fileno(), 'rt', encoding='latin-1',
                     closefd=False)

    client_out = open(client_sock.fileno(), 'wt', encoding='latin-1',
                      closefd=False)

    # Echo lines back to the client using file I/O
    for line in client_in:
        client_out.write(line)
        client_out.flush()

    client_sock.close()


def echo_server(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(address)
    sock.listen(1)
    while True:
        client, addr = sock.accept()
        echo_client(client, addr)


# 可以使用这种技术来构造一个别名，以不同于第一次打开文件的方式使用它。
# 下面的例子演示输出二进制数据到标准输出(通常以文本模式打开)
bstdout = open(sys.stdout.fileno(), 'wb', closefd=False)
bstdout.write(b'hh ww\n')
bstdout.flush()
