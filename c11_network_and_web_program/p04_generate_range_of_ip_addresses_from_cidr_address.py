""" 通过CIDR地址生成对应的IP地址集 """

import ipaddress


# 使用ipaddress模块
net = ipaddress.ip_network('123.45.67.64/27')
print(net, type(net))
for a in net:
    print(a)
print()

net6 = ipaddress.ip_network('12:3456:78:90ab:cd:ef01:23:30/125')
print(net6, type(net6))
for a in net6:
    print(a)
print()

# Network允许像数组一样的索引取值
print(net.num_addresses)
print(net[0])
print(net[-1])
print()

# 还可以执行网络成员检查之类的操作
print(ipaddress.ip_address('123.45.67.69') in net)
print(ipaddress.ip_address('123.45.67.123') in net)
print()

# 一个IP地址和网络地址能通过一个IP接口来指定
inet = ipaddress.ip_interface('123.45.67.73/27')
print(inet.network)
print(inet.ip)
