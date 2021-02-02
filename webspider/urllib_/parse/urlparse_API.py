from urllib.parse import urlparse
# urllib.parse.urlparse(urlstring, scheme='', allow_fragments=True)
# urlstring: 必填，即解析的URL
# scheme: 默认的协议,不带URL时生效
res = urlparse('www.baidu.com/index.html;user?id=5#comment', scheme='https')
print(res)
# allow_fragments， True:允许fragments (默认)
re = urlparse('www.baidu.com/index.html;user?id=5#comment', scheme='https', allow_fragments=False)
print(re)
