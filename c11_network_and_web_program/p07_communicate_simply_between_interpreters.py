""" 在不同的Python解释器之间交互 """

from multiprocessing.connection import Listener
import traceback


# 使用 multiprocessing.connection 模块实现解释器之间的通信
def echo_client(conn):
    try:
        while True:
            msg = conn.recv()
            conn.send(msg)
    except EOFError:
        print('Connection closed')


def echo_server(address, authkey):
    serv = Listener(address, authkey=authkey)
    while True:
        try:
            client = serv.accept()

            echo_client(client)
        except Exception:
            traceback.print_exc()


echo_server(('', 25000), authkey=b'peekaboo')


# 客户端连接服务器并发送消息
"""
>>> from multiprocessing.connection import Client
>>> c = Client(('localhost', 25000), authkey=b'peekaboo')
>>> c.send('hello')
>>> c.recv()
'hello'
>>> c.send(42)
>>> c.recv()
42
>>> c.send([1, 2, 3, 4, 5])
>>> c.recv()
[1, 2, 3, 4, 5]
>>>
"""


# 目前有很多用来实现各种消息传输的包和函数库，比如ZeroMQ、Celery等。 还有另外一种选择就是自己在底层socket基础之上来实现一个消息传输层。
# 但是想要简单一点的方案，那么这时候 multiprocessing.connection 就派上用场了。仅仅使用一些简单的语句即可实现多个解释器之间的消息通信。


# 如果需要对底层连接做更多的控制，比如需要支持超时、非阻塞I/O或其他类似的特性，最好使用另外的库或者是在高层socket上来实现这些特性。
