from urllib.parse import urlunsplit

# 必须是5个参数
data = ['https', 'www.baidu.com', 'index.html', 'a=6', 'comment']
print(urlunsplit(data))
