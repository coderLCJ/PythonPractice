from urllib.parse import urlparse
# 实现URL的识别和分段
res = urlparse('https://www.baidu.com/index.html;user?id=5#comment')
print(type(res), res)

# scheme://netloc/path;params?query#fragmemnt

