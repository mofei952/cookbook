import select


class EventHandler:
    def fileno(self):
        'Return the associated file descriptor'
        raise NotImplementedError('must implement')

    def wants_to_receive(self):
        'Return True if receiving is allowed'
        return False

    def handle_receive(self):
        'Perform the receive operation'
        pass

    def wants_to_send(self):
        'Return True if sending is requested'
        return False

    def handle_send(self):
        'Send outgoing data'
        pass


def event_loop(handlers):
    while True:
        wants_recv = [h for h in handlers if h.wants_to_receive()]
        wants_send = [h for h in handlers if h.wants_to_send()]
        can_recv, can_send, _ = select.select(wants_recv, wants_send, [])
        # print(can_recv, can_send)
        for h in can_recv:
            h.handle_receive()
        for h in can_send:
            h.handle_send()


# 事件循环的关键部分是 select() 调用，它会不断轮询文件描述符从而激活它。
# 在调用 select() 之前，事件循环会询问所有的处理器来决定哪一个想接受或发生。
# 然后它将结果列表提供给 select() 。然后 select() 返回准备接受或发送的对象组成的列表。
# 然后相应的 handle_receive() 或 handle_send() 方法被触发。
