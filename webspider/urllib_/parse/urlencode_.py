from urllib.parse import urlencode

# 构造GET请求参数时非常有用
params = {
    'name': 'laity',
    'age': 23
}
base_url = 'https://www.baidu.com?'
url = base_url + urlencode(params)
print(url)
