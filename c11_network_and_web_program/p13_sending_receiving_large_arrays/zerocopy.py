# 利用 memoryviews 来发送和接受大数组
def send_from(arr, dest):
    view = memoryview(arr).cast('B')
    while len(view):
        nsent = dest.send(view)
        view = view[nsent:]


def recv_into(arr, source):
    view = memoryview(arr).cast('B')
    while len(view):
        nrecv = source.recv_into(view)
        print(nrecv)
        view = view[nrecv:]

# 本质上，一个内存视图就是一个已存在数组的覆盖层。
# 不仅仅是那样， 内存视图还能以不同的方式转换成不同类型来表现数据。

# 我们使用很多不同的 send() 和 recv_into() 来传输整个数组。
# 不用担心，每次操作后，视图会通过发送或接受字节数量被切割成新的视图。
# 新的视图同样也是内存覆盖层。因此，还是没有任何的复制操作。
