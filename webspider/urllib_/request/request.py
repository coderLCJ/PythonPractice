import urllib.request

request = urllib.request.Request('https://www.baidu.com')
# 将参数封装成Request对象
response = urllib.request.urlopen(request)
print(response.read().decode('utf8'))

