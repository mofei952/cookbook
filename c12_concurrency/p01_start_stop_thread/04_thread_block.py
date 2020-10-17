import socket
from socket import AF_INET, SOCK_STREAM
from threading import Thread
import time


# 如果线程执行一些像I/O这样的阻塞操作，那么通过轮询来终止线程将使得线程之间的协调变得非常棘手。
# 比如，如果一个线程一直阻塞在一个I/O操作上，它就永远无法返回，也就无法检查自己是否已经被结束了。
# 要正确处理这些问题，需要利用超时循环来小心操作线程。
class IOTask:
    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False

    def run(self, sock):
        sock.settimeout(5)
        while self._running:
            try:
                data = sock.recv(8192)
                print(data)
            except socket.timeout:
                continue


sock = socket.socket(AF_INET, SOCK_STREAM)
sock.bind(('', 20000))
sock.listen(5)


client_sock, client_addr = sock.accept()
task = IOTask()
t = Thread(target=task.run, args=(client_sock, ))
t.start()

time.sleep(10)
task.terminate()


# 在交互式命令行中执行以下代码
"""
>>> from socket import socket, AF_INET, SOCK_STREAM
>>> s = socket(AF_INET, SOCK_STREAM)
>>> s.connect(('localhost', 20000))
>>> s.send(b'hello')
5
>>>
"""
