from urllib import request, parse

url = 'http://httpbin.org/post'
headers = {
    'User-Agent': 'Mozilla/4.0(compatible; MSIE 5.5; Windows NT)',
    'Host': 'httpbin.org'
}
dicts = {
    'name': 'Laity'
}
data = bytes(parse.urlencode(dicts), encoding='utf8')
req = request.Request(url=url, data=data, headers=headers, method='POST')
#  headers也可以通过add_header()方法添加
#  req = request.Request(url=url, data=data, method='POST')
#  req.add_header('User-Agent', 'Mozilla/4.0(compatible; MSIE 5.5; Windows NT')
response = request.urlopen(req)
print(response.read().decode('utf8'))
