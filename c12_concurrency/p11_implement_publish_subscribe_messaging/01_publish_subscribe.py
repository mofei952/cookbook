from c12_concurrency.p11_implement_publish_subscribe_messaging.exchange import get_exchange


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
