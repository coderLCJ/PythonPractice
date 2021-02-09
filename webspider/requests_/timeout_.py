import requests

r = requests.get('https://www.baidu.com', timeout=1)
print(r.text)
