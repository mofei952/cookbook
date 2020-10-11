from socket import AF_INET, SOCK_STREAM, socket

import numpy

from zerocopy import send_from

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 25000))
s.listen(1)
client, addr = s.accept()

a = numpy.arange(0.0, 50000000.0)
send_from(a, client)
