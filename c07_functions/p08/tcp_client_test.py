#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2020/4/8 21:10
# @File    : tcp_client_test.py
# @Software: PyCharm

from socket import socket, AF_INET, SOCK_STREAM

s = socket(AF_INET, SOCK_STREAM)
s.connect(('127.0.0.1', 15000))
while True:
    msg = input('>>')
    if msg == 'quit':
        break

    msg += '\n'
    s.send(msg.encode())

    recv_data = s.recv(1024)
    print(recv_data.decode())

s.close()
