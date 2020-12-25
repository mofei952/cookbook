# 如果放宽对于同步和异步消息发送的要求，类actor对象还可以通过生成器来简化定义
def print_actor():
    while True:
        try:
            msg = yield
            print('Got:', msg)
        except GeneratorExit:
            print('Actor terminating')
            raise


p = print_actor()
next(p)
p.send('Hello')
p.send('World')
p.close()
