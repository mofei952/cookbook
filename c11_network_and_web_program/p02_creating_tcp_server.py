""" 创建TCP服务器 """

from socket import AF_INET, SOCK_STREAM, socket
from socketserver import (BaseRequestHandler, StreamRequestHandler, TCPServer,
                          ThreadingTCPServer)
from threading import Thread


# 使用socketserver库创建一个TCP服务器
# class EchoHandler(BaseRequestHandler):
#     def handle(self):
#         print('Got connection from', self.client_address)
#         while True:
#             msg = self.request.recv(8192)
#             if not msg:
#                 break
#             self.request.send(msg)


# serv = TCPServer(('', 20000), EchoHandler)
# serv.serve_forever()


# 在交互式命令行中执行以下代码
"""
>>> from socket import socket, AF_INET, SOCK_STREAM
>>> s = socket(AF_INET, SOCK_STREAM)
>>> s.connect(('localhost', 20000))
>>> s.send(b'hello')
5
>>> s.recv(8192)
b'hello'
>>>
"""


# 使用StreamRequestHandler基类将一个类文件接口放置在底层socket上
class EchoHandler(StreamRequestHandler):
    def handle(self):
        print('Got connection from', self.client_address)
        for line in self.rfile:
            print(line)
            self.wfile.write(line)


# serv = TCPServer(('', 20000), EchoHandler)
# serv.serve_forever()


# 在交互式命令行中执行以下代码
"""
>>> from socket import socket, AF_INET, SOCK_STREAM
>>> s = socket(AF_INET, SOCK_STREAM)
>>> s.connect(('localhost', 20000))
>>> s.send(b'hello\n')
6
>>> s.recv(8192)
b'hello\n'
>>>
"""


# 如果要处理多个客户端，可以初始化一个ForkingTCPServer或者是ThreadingTCPServer
# serv = ThreadingTCPServer(('', 20000), EchoHandler)
# serv.serve_forever()


# 使用fork或线程服务器有个潜在问题就是它们会为每个客户端连接创建一个新的进程或线程。
# 由于客户端连接数是没有限制的，因此一个恶意的黑客可以同时发送大量的连接让你的服务器奔溃。
# 如果担心这个问题，可以创建一个预先分配大小的工作线程池或进程池。
# 先创建一个普通的非线程服务器，然后在一个线程池中使用 serve_forever() 方法来启动它们
# NWORKERS = 16
# serv = TCPServer(('', 20000), EchoHandler)
# for n in range(NWORKERS):
#     t = Thread(target=serv.serve_forever)
#     t.daemon = True
#     t.start()
# serv.serve_forever()


# 使用socket库来实现TCP服务器
def echo_handler(address, client_sock):
    print('Got connection from {}'.format(address))
    while True:
        msg = client_sock.recv(8192)
        if not msg:
            break
        client_sock.sendall(msg)
    client_sock.close()


def echo_server(address, backlog=5):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(address)
    sock.listen(backlog)
    while True:
        client_sock, client_addr = sock.accept()
        echo_handler(client_addr, client_sock)


echo_server(('', 20000))
