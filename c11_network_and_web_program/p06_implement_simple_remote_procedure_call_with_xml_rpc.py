""" 通过XML-RPC实现简单的远程调用 """

from xmlrpc.server import SimpleXMLRPCServer


# 演示一下一个实现了键-值存储功能的简单服务器
class KeyValueServer:
    _rpc_methods_ = ['get', 'set', 'delete', 'exists', 'keys']

    def __init__(self, address):
        self._data = {}
        self._serv = SimpleXMLRPCServer(address, allow_none=True)
        for name in self._rpc_methods_:
            self._serv.register_function(getattr(self, name))

    def get(self, name):
        return self._data[name]

    def set(self, name, value):
        self._data[name] = value

    def delete(self, name):
        del self._data[name]

    def exists(self, name):
        return name in self._data

    def keys(self):
        return list(self._data)

    def serve_forever(self):
        self._serv.serve_forever()


kvserv = KeyValueServer(('', 15000))
kvserv.serve_forever()


# 从一个客户端机器上面来访问服务器
"""
>>> from xmlrpc.client import ServerProxy
>>> s = ServerProxy('http://localhost:15000', allow_none=True)
>>> s.set('foo', 'bar')
>>> s.set('spam', [1, 2, 3])
>>> s.keys()
['spam', 'foo']
>>> s.get('foo')
'bar'
>>> s.get('spam')
[1, 2, 3]
>>> s.delete('spam')
>>> s.exists('spam')
False
>>>
"""


# XML-RPC暴露出来的函数只能适用于部分数据类型，比如字符串、整形、列表和字典。
# 对于其他类型就得需要做些额外的功课了，如果想通过 XML-RPC 传递一个对象实例，实际上只有他的实例字典被处理
"""
>>> class Point:
...     def __init__(self, x, y):
...             self.x = x
...             self.y = y
...
>>> p = Point(2, 3)
>>> s.set('foo', p)
>>> s.get('foo')
{'x': 2, 'y': 3}
>>>
"""

# 类似的，对于二进制数据的处理也不太一样
"""
>>> s.set('foo', b'Hello World')
>>> s.get('foo')
<xmlrpc.client.Binary object at 0x10131d410>

>>> _.data
b'Hello World'
>>>
"""
