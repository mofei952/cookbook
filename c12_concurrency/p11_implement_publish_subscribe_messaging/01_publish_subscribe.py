from c12_concurrency.p11_implement_publish_subscribe_messaging.exchange import get_exchange


class Task:
    def send(self, msg):
        print(self, msg)


task_a = Task()
task_b = Task()

exc = get_exchange('name')
with exc.subscribe(task_a, task_b):
    exc.send('msg1')
    exc.send('msg2')
print()


class DisplayMessages:
    def __init__(self):
        self.count = 0

    def send(self, msg):
        self.count += 1
        print('msg[{}]: {!r}'.format(self.count, msg))


d = DisplayMessages()
exc = get_exchange('name')
with exc.subscribe(d):
    exc.send('ttt')
    exc.send('aaa')
