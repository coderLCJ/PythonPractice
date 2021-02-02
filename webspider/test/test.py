import urllib.request

response = urllib.request.urlopen('https://www.baidu.com')
print(response.status)
print(response.getheaders())        # 请求头信息
print(response.getheader('Server'))     # 服务器用什么搭建的
