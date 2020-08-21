""" 作为客户端与HTTP服务交互 """

from urllib import request, parse
import requests


# 使用 urllib.request 模块
url = 'http://httpbin.org/get'
parms = {
    'name1': 'value1',
    'name2': 'value2'
}
querystring = parse.urlencode(parms)
u = request.urlopen(url+'?' + querystring)
resp = u.read()
print(resp)


# 发送POST请求
url = 'http://httpbin.org/post'
parms = {
    'name1': 'value1',
    'name2': 'value2'
}
querystring = parse.urlencode(parms)
u = request.urlopen(url, querystring.encode('ascii'))
resp = u.read()
print(resp)


# 在发出的请求中加入一些自定义的HTTP头
headers = {
    'User-agent': 'none/ofyourbusiness',
    'Spam': 'Eggs'
}
req = request.Request(url, querystring.encode('ascii'), headers=headers)
u = request.urlopen(req)
resp = u.read()
print(resp)


# 使用requests库
url = 'http://httpbin.org/post'
parms = {
    'name1': 'value1',
    'name2': 'value2'
}
headers = {
    'User-agent': 'none/ofyourbusiness',
    'Spam': 'Eggs'
}
resp = requests.post(url, data=parms, headers=headers)
text = resp.text
print(text)


# 使用requests库发起一个HEAD请求，并从响应中提取出一些HTTP头数据的字段
resp = requests.head('https://www.python.org')
status = resp.status_code
print(status)
print(resp.headers['Content-Type'])
print(resp.headers['Content-Length'])
