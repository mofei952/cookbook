import time


def countdown(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(1)
