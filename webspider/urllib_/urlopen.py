import urllib.request
import urllib.parse
import urllib.error
import socket

# 请求服务器
response = urllib.request.urlopen('https://www.baidu.com')
print(response.status)                  # 状态码
# print(response.getheaders())        # 请求头信息
print(response.getheader('Server'))     # 服务器用什么搭建的

# 传入参数
data = bytes(urllib.parse.urlencode({'word': 'Hello'}), encoding='utf8')
response = urllib.request.urlopen('http://httpbin.org/post', data=data)
print(response.read())

# 设置超时时间
response = urllib.request.urlopen('http://httpbin.org/get', timeout=10)
print(response.read())
# 用try except实现超时跳过爬取
try:
    response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.01)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('访问超时')
