from threading import Thread, Event
import time


# 使用 threading 库中的 Event 对象
def countdown(n, started_evt):
    print('countdown starting')
    started_evt.set()
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(5)


started_evt = Event()

print('Launching countdown')
t = Thread(target=countdown, args=(10, started_evt))
t.start()

# 等待countdown()函数输出启动信息后，才能继续执行
started_evt.wait()
print('countdown is running')
