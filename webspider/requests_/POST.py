import requests

data = {'name': 'laity', 'age': 21}
r = requests.post('http://httpbin.org/post', data=data)
print(r.text)
# form部分为提交的数据

