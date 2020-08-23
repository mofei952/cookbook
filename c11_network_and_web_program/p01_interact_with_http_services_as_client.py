""" 作为客户端与HTTP服务交互 """

from urllib import request, parse
import requests


# # 使用 urllib.request 模块
# url = 'http://httpbin.org/get'
# parms = {
#     'name1': 'value1',
#     'name2': 'value2'
# }
# querystring = parse.urlencode(parms)
# u = request.urlopen(url + '?' + querystring)
# resp = u.read()
# print(resp)


# # 发送POST请求
# url = 'http://httpbin.org/post'
# parms = {
#     'name1': 'value1',
#     'name2': 'value2'
# }
# querystring = parse.urlencode(parms)
# u = request.urlopen(url, querystring.encode('ascii'))
# resp = u.read()
# print(resp)


# # 在发出的请求中加入一些自定义的HTTP头
# headers = {
#     'User-agent': 'none/ofyourbusiness',
#     'Spam': 'Eggs'
# }
# req = request.Request(url, querystring.encode('ascii'), headers=headers)
# u = request.urlopen(req)
# resp = u.read()
# print(resp)


# # 使用requests库
# url = 'http://httpbin.org/post'
# parms = {
#     'name1': 'value1',
#     'name2': 'value2'
# }
# headers = {
#     'User-agent': 'none/ofyourbusiness',
#     'Spam': 'Eggs'
# }
# resp = requests.post(url, data=parms, headers=headers)
# print(resp.content)  # 原始的二进制数据
# print(resp.text)  # 以unicode解码的文本
# print(resp.json())  # json格式的响应内容


# # 使用requests库发起一个HEAD请求，并从响应中提取出一些HTTP头数据的字段
# resp = requests.head('https://www.python.org')
# status = resp.status_code
# print(status)
# print(resp.headers['Content-Type'])
# print(resp.headers['Content-Length'])


# # 用requests库通过基本认证登录Pypi
# resp = requests.get('http://pypi.python.org/pypi?:action=login',
#                     auth=('user', 'password'))
# print(resp.status_code)
# print(resp.text)


# # 用requests库将HTTP cookies从一个请求传递到另一个请求
# resp1 = requests.get('https://www.baidu.com')
# print(resp1.cookies)
# resp2 = requests.get('https://www.baidu.com', cookies=resp1.cookies)
# print(resp2.text)


# 用requests上传内容
url = 'http://httpbin.org/post'
files = {'file': ('data.csv', open('p01/data.csv', 'rb'))}
r = requests.post(url, files=files)
print(r.text)
