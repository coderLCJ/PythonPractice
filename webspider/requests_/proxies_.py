import requests

proxies = {
    'http': '',
    'https': ''
}
# 暂时没有代理服务器

r = requests.get('https://www.baidu.com', proxies=proxies)
print(r.text)

