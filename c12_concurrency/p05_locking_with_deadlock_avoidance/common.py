import threading
from contextlib import contextmanager


# 解决死锁问题的一种方案是为程序中的每一个锁分配一个唯一的id，
# 然后只允许按照升序规则来使用多个锁
# 这个规则使用上下文管理器 是非常容易实现的
_local = threading.local()


@contextmanager
def acquire(*locks):
    # Sort locks
    locks = sorted(locks, key=id)

    acquired = getattr(_local, 'acquired', [])
    if acquired and max(id(lock) for lock in acquired) > id(locks[0]):
        raise RuntimeError('Lock Order Violation')

    acquired.extend(locks)
    # _local.acquired = acquired

    try:
        for lock in locks:
            lock.acquire()
        yield
    finally:
        for lock in reversed(locks):
            lock.release()
        del acquired[-len(locks):]
