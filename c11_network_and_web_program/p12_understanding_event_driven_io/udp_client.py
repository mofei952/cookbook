from socket import socket, AF_INET, SOCK_DGRAM

s = socket(AF_INET, SOCK_DGRAM)
s.sendto(b'', ('localhost', 14000))
msg = s.recvfrom(128)
print(msg)

s.sendto(b'Hello', ('localhost', 15000))
msg = s.recvfrom(128)
print(msg)
