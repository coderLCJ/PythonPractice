from urllib.parse import urljoin

# urljoin(base, url, allow_fragments)
# 作用：用url对base进行补充， 如果是一个新链接，则base失效
print(urljoin('http://www.baidu.com', 'index.html'))
print(urljoin('http://www.baidu,com', 'http://www.google.com'))
