from urllib import request, error
import socket
# 更加精确的判断错误类型
try:
    res = request.urlopen('https://colcj.github.io/', timeout=0.1)
except error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('访问超时')
    else:
        print(e.reason)
else:
    print('Request successfully')
