from concurrent.futures import ThreadPoolExecutor
import urllib.request


# 使用 ThreadPoolExecutor 相对于手动实现的一个好处在于它使得
# 任务提交者更方便的从被调用函数中获取返回值。
def fetch_url(url):
    u = urllib.request.urlopen(url)
    data = u.read()
    return data


pool = ThreadPoolExecutor(10)
# Submit work to the pool
a = pool.submit(fetch_url, 'http://www.python.org')
b = pool.submit(fetch_url, 'http://www.pypy.org')

# Get the results back
x = a.result()
y = b.result()

print(x)
print(y)

# 例子中返回的handle对象会帮你处理所有的阻塞与协作，然后从工作线程中返回数据给你
# a.result() 操作会阻塞进程直到对应的函数执行完成并返回一个结果。
