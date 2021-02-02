from urllib.parse import parse_qs, parse_qsl

# 反序列化 转换为字典
params = 'name=laity&age=12'
print(parse_qs(params))
# 转换为列表
print(parse_qsl(params))
