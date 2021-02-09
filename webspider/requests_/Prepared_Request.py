from requests import Request, Session

url = 'http://httpbin.org/post'
data = {
    'name': 'laity',
    'age': 21
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}

s = Session()
req = Request('POST', url, data=data, headers=headers)
p = s.prepare_request(req)
r = s.send(p)
print(r.text)
