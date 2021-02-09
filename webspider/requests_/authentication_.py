import requests

# 弹出身份验证窗口时使用
r = requests.get('http://localhost:5000', auth=('username', 'password'))
print(r.status_code)
