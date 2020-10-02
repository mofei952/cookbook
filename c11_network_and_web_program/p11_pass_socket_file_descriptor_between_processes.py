""" 进程间传递Socket文件描述符 """

import multiprocessing
from multiprocessing.reduction import recv_handle, send_handle
import socket


def worker(in_p, out_p):
    out_p.close()
    while True:
        fd = recv_handle(in_p)
        print('CHILD: GOT FD', fd)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM, fileno=fd) as s:
            while True:
                msg = s.recv(1024)
                if not msg:
                    break
                print('CHILD: RECV {!r}'.format(msg))
                s.send(msg)


def server(address, in_p, out_p, worker_pid):
    in_p.close()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    s.bind(address)
    s.listen(1)
    while True:
        client, addr = s.accept()
        print('SERVER: Got connection from', addr)
        send_handle(out_p, client.fileno(), worker_pid)
        client.close()


if __name__ == "__main__":
    c1, c2 = multiprocessing.Pipe()
    worker_p = multiprocessing.Process(target=worker, args=(c1, c2))
    worker_p.start()

    server_p = multiprocessing.Process(target=server,
                                       args=(('', 15000), c1, c2, worker_p.pid))
    server_p.start()

    c1.close()
    c2.close()


# 客户端执行
"""
>>> from multiprocessing.connection import Client
>>> c = Client(('localhost', 15000))
>>> c.send('hello')
>>> c.recv()
'hello'
"""

# 对于大部分程序员来讲在不同进程之间传递文件描述符好像没什么必要。 但是，有时候它是构建一个可扩展系统的很有用的工具。
# 例如，在一个多核机器上面， 你可以有多个Python解释器实例，将文件描述符传递给其它解释器来实现负载均衡。
