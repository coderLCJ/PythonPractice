import requests

requests.get('http://httpbin.org/cookies/set/number/123456789')
r = requests.get('http://httpbin.org/cookies')
# 并不能获取cookies 相当于开启两个浏览器 此时需要用到会话维持
print(r.text)

s = requests.Session()
s.get('http://httpbin.org/cookies/set/number/123456789')
# 成功获取设置的cookies
# 通常用于模拟成功登录后进一步操作
r = s.get('http://httpbin.org/cookies')
print(r.text)
