class NetworkError(Exception):
    pass


class HostnameError(NetworkError):
    pass


class TimeoutError(NetworkError):
    pass


class ProtocolError(NetworkError):
    pass


try:
    # msg = s.recv()
    raise TimeoutError('xxx')
except TimeoutError as e:
    print('Time out: ', e)
except ProtocolError as e:
    print('Protocol error: ', e)


try:
    raise RuntimeError('It failed')
except RuntimeError as e:
    print(e.args)

try:
    raise RuntimeError('It failed', 42, 'spam')
except RuntimeError as e:
    print(e.args)
