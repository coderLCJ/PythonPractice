from urllib import request, error
try:
    # 打开一个不存在的页面
    res = request.urlopen('https://www.baidu.com/Laity.html')
    print(res.read())
except error.URLError as e:
    print(e.reason)
