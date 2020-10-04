from multiprocessing.connection import Client


c = Client(('localhost', 15000))
c.send('hello')
c.recv()
