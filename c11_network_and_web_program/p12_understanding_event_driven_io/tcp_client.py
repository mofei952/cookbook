from socket import socket, AF_INET, SOCK_STREAM

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 16000))
s.send(b'hello')
msg = s.recv(8192)
print(msg)
