from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener

proxy = ProxyHandler({
    'http': 'http://192.168.43.1:1234',
    'https': 'https://192.168.43.1:1234'
})
opener = build_opener(proxy)
try:
    res = opener.open('http://fanyi.youdao.com/')
    print(res.read().decode('utf8'))
except URLError as e:
    print(e.reason)
# [WinError 10060] 由于连接方在一段时间后没有正确答复或连接的主机没有反应，连接尝试失败。
