from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
from urllib.error import URLError
# 验证用户名和密码
username = '2907805535@qq.com'
password = 'password'
url = 'https://pintia.cn/auth/login?redirect=https%3A%2F%2Fwww.patest.cn%2Fpractice'

p = HTTPPasswordMgrWithDefaultRealm()
p.add_password(None, url, username, password)
auth_handler = HTTPBasicAuthHandler(p)
opener = build_opener(auth_handler)

try:
    res = opener.open(url)
    html = res.read().decode('utf8')
    f = open('html.txt', 'w')
    f.write(html)
except URLError as e:
    print(e.reason)
