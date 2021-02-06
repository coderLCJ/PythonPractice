import requests

r = requests.get('http://httpbin.org/get')
print(r.text)

# 添加额外信息
data = {
    'name': 'laity',
    'age': 21
}
r = requests.get('http://httpbin.org/get', params=data)
print(r.text)
# 返回的是JSON格式 调用json()函数 转换为字典格式
print(r.json())
print(type(r.json()))
