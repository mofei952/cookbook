""" 在网络服务中加入SSL """

from socket import socket, AF_INET, SOCK_STREAM
import ssl


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


echo_server(('', 20000))


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
