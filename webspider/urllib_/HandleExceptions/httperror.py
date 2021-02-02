from urllib import request, error

try:
    res = request.urlopen('https://colcj.github.io/')
except error.HTTPError as e:
    print(e.reason, e.code, e.headers, sep='\n')
except error.URLError as e:
    print(e.reason)
else:
    print('Request successfully')
