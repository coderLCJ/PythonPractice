import requests

r = requests.get('http://www.baidu.com')
print(type(r.status_code), r.status_code)
print(type(r.headers), r.headers)
print(type(r.cookies), r.cookies)
print(r.url)
print(r.history)
# 状态码查询对象 request.codes
exit() if not r.status_code == requests.codes.ok else print('Request successful')
