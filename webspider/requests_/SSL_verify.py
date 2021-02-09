import requests
from requests.packages import urllib3

# 1、 设置忽略警告
urllib3.disable_warnings()
# 2、捕获警告到日志
# 3、指定本地证书

r = requests.get('https://www.12306.cn', verify=False)  # 关闭证书验证 但是会有警告
print(r.status_code)
