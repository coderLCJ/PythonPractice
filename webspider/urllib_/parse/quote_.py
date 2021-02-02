from urllib.parse import quote, unquote
from selenium import webdriver

# 将内容转换为URL的编码格式
key = '壁纸'
url = 'https://www.baidu.com/s?wd=' + quote(key)
print(url)
# 解码
print(unquote(url))


# 在浏览器打开测试
# web = webdriver.Chrome()
# web.get(url)
