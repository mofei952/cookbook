""" 在网络服务中加入SSL """

import ssl
from socket import AF_INET, SOCK_STREAM, socket
from xmlrpc.server import SimpleXMLRPCServer


# 生成初始配置key、证书
# 在创建证书的时候，各个值的设定可以是任意的，但是”Common Name“的值通常要包含服务器的DNS主机名。
# 如果只是在本机测试，那么就使用”localhost“，否则使用服务器的域名。
r"""
$env:OPENSSL_CONF="E:\software\Git\usr\ssl\openssl.cnf"
openssl req -new -x509 -days 365 -nodes -out server_cert.pem -keyout server_key.pem
"""


# 通过SSL协议认证并加密传输的数据
KEYFILE = 'p10\server_key.pem'
CERTFILE = 'p10\server_cert.pem'


def echo_client(s):
    while True:
        data = s.recv(8192)
        if data == b'':
            break
        s.send(data)
    s.close()
    print('Connection closed')


def echo_server(address):
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(address)
    s.listen(1)

    s_ssl = ssl.wrap_socket(s, keyfile=KEYFILE,
                            certfile=CERTFILE, server_side=True)
    while True:
        try:
            c, a = s_ssl.accept()
            print('Got connection', c, a)
            echo_client(c)
        except Exception as e:
            print('{}: {}'.format(e.__class__.__name__, e))


# echo_server(('', 20000))


# 在客户端请求服务器来认证并确认连接
"""
>>> from socket import socket, AF_INET, SOCK_STREAM
>>> import ssl
>>> s = socket(AF_INET, SOCK_STREAM)
>>> s_ssl = ssl.wrap_socket(s,
                cert_reqs=ssl.CERT_REQUIRED,
                ca_certs = 'server_cert.pem')
>>> s_ssl.connect(('localhost', 20000))
>>> s_ssl.send(b'Hello World?')
12
>>> s_ssl.recv(8192)
b'Hello World?'
>>>
"""


# 可以通过一个mixin类来为服务器添加SSL
class SSLMixin:
    '''
    Mixin class that adds support for SSL to existing servers based
    on the socketserver module.
    '''

    def __init__(self, *args,
                 keyfile=None, certfile=None, ca_certs=None,
                 cert_reqs=ssl.CERT_NONE,
                 **kwargs):
        self._keyfile = keyfile
        self._certfile = certfile
        self._ca_certs = ca_certs
        self._cert_reqs = cert_reqs
        super().__init__(*args, **kwargs)

    def get_request(self):
        client, addr = super().get_request()
        client_ssl = ssl.wrap_socket(client,
                                     keyfile=self._keyfile,
                                     certfile=self._certfile,
                                     ca_certs=self._ca_certs,
                                     cert_reqs=self._cert_reqs,
                                     server_side=True)
        return client_ssl, addr


class SSLSimpleXMLRPCServer(SSLMixin, SimpleXMLRPCServer):
    pass


class KeyValueServer:
    _rpc_methods_ = ['get', 'set', 'delete', 'exists', 'keys']

    def __init__(self, *args, **kwargs):
        self._data = {}
        self._serv = SSLSimpleXMLRPCServer(*args, allow_none=True, **kwargs)
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


KEYFILE = 'p10\server_key.pem'
CERTFILE = 'p10\server_cert.pem'
kvserv = KeyValueServer(('localhost', 15000),
                        keyfile=KEYFILE,
                        certfile=CERTFILE)
kvserv.serve_forever()


# 可以使用普通的xmlrpc.client模块来连接，只需要在URL中指定https:即可
"""
>>> import ssl
>>> ssl._create_default_https_context = ssl._create_unverified_context
>>> from xmlrpc.client import ServerProxy
>>> s = ServerProxy('https://localhost:15000', allow_none=True)
>>> s.set('foo','bar')
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


# 建立一个安全的XML-RPC连接来确认服务器证书
"""
import ssl
from socket import AF_INET, SOCK_STREAM, socket
from xmlrpc.client import SafeTransport, ServerProxy

class VerifyCertSafeTransport(SafeTransport):
    def __init__(self, cafile, certfile=None, keyfile=None):
        SafeTransport.__init__(self)
        self._ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
        self._ssl_context.load_verify_locations(cafile)
        if certfile:
            self._ssl_context.load_cert_chain(certfile, keyfile)
        self._ssl_context.verify_mode = ssl.CERT_REQUIRED
        self.context = self._ssl_context
    def make_connection(self, host):
        # Items in the passed dictionary are passed as keyword
        # arguments to the http.client.HTTPSConnection() constructor.
        # The context argument allows an ssl.SSLContext instance to
        # be passed with information about the SSL configuration
        s = super().make_connection((host))
        return s


# Create the client proxy
s = ServerProxy('https://localhost:15000',
                transport=VerifyCertSafeTransport('server_cert.pem'),
                allow_none=True)
"""
