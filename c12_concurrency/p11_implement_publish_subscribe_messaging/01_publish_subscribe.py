from collections import defaultdict


# 要实现发布/订阅的消息通信模式，
# 通常要引入一个单独的“交换机”或“网关”对象作为所有消息的中介。
class Exchange:
    def __init__(self):
        self._subscribers = set()

    def attach(self, task):
        self._subscribers.add(task)

    def detach(self, task):
        self._subscribers.remove(task)

    def send(self, msg):
        for subscriber in self._subscribers:
            subscriber.send(msg)


_exchanges = defaultdict(Exchange)


def get_exchange(name):
    return _exchanges[name]


class Task:
    def send(self, msg):
        print(self, msg)


task_a = Task()
task_b = Task()

exc = get_exchange('name')
exc.attach(task_a)
exc.attach(task_b)

exc.send('msg1')
exc.send('msg2')

exc.detach(task_a)
exc.detach(task_b)
