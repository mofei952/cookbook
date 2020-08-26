""" 创建UDP服务器 """

import time
from socket import AF_INET, SOCK_DGRAM, socket
from socketserver import BaseRequestHandler, ThreadingUDPServer, UDPServer


# 使用socketserver库创建UDP服务器
class TimeHandler(BaseRequestHandler):
    def handle(self):
        print('Got connection from', self.client_address)
        msg, sock = self.request
        resp = time.ctime()
        print(resp)
        sock.sendto(resp.encode('ascii'), self.client_address)


# serv = UDPServer(('', 20000), TimeHandler)
# serv.serve_forever()


# 在交互式命令行中输入以下代码
"""
>>> from socket import socket, AF_INET, SOCK_DGRAM
>>> s = socket(AF_INET, SOCK_DGRAM)
>>> s.sendto(b'', ('localhost', 20000))
0
>>> s.recvfrom(8192)
(b'Wed Aug 15 20:35:08 2012', ('127.0.0.1', 20000))
>>>
"""

# UDPServer 类是单线程的，也就是说一次只能为一个客户端连接服务
# 如果要并发操作，可以实例化一个ForkingUDPServer或ThreadingUDPServer
# serv = ThreadingUDPServer(('', 20000), TimeHandler)
# serv.serve_forever()


# 也可以使用 socket 来实现一个UDP服务器
def time_server(address):
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.bind(address)
    while True:
        msg, addr = sock.recvfrom(8192)
        print('Got message from', addr)
        resp = time.ctime()
        sock.sendto(resp.encode('ascii'), addr)


time_server(('', 20000))
