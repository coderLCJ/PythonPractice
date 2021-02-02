from urllib.parse import urlsplit

# 与urlparse类似 但是不单独解析params 只返回5个结果
# params会并入path中
res = urlsplit('https://www.baidu.com/index.html;user?id=5#comment')
print(res)
# 可以用属性或者下标获取值
print(res.scheme, res[0])
