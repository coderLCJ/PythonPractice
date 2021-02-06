import requests

r = requests.get('https://github.com/favicon.ico')
# print(r.text) 乱码
# print(r.content) 二进制数据
# 将图标保存下来
with open('favicon.ico', 'wb') as f:
    f.write(r.content)
