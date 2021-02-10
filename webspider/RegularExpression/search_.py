import re
# match是从开头开始匹配的 而search是遍历整个字符串

content = 'Extra string Hello 1234567 World_This is Regex Demo'
res = re.search('He.*?(\d+).*?Demo$', content)
print(res.group(1))

# 匹配失败
res = re.match('He.*?(\d+).*?Demo$', content)
print(res)
