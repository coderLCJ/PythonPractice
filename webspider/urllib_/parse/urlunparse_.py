from urllib.parse import urlunparse

# 必须是6个参数
data = ['https', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']
print(urlunparse(data))
