import re

content = 'Hello 123 4567 World_This is a Regex Demo'
print(len(content))
res = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}', content)
print(res)
print(res.group())      # 输出匹配内容
print(res.span())       # 输出匹配范围

print('--------------------------------')

# 提取部分内容 用（）括起来
res = re.match('^Hello\s(\d{3})\s(\d{4})', content)
print(res.group())
print(res.group(1))     # 输出第一个括号匹配的内容
print(res.group(2))     # 输出第二个括号匹配的内容

print('--------------------------------')

# 通配符'.*', '.'匹配任意字符（除换行符） '*'代表前面的字符可以匹配无限次
res = re.match('^Hello.*Demo$', content)
print(res.group())

print('--------------------------------')

# 贪婪: .*, 非贪婪: .*?
content = 'Hello 1234567 this is Demo'
res = re.match('^He.*(\d+).*Demo$', content)
print(res.group(1))     # 贪婪：.*会尽可能的匹配多的字符 所以只得到7

res = re.match('^He.*?(\d+).*Demo$', content)
print(res.group(1))     # 非贪婪 .*? 尽可能匹配少的字符

print('--------------------------------')

# 修饰符
content = '''Hello 1234567 World_This
    is a Regex Demo
'''
res = re.match('^He.*?(\d+).*?Demo$', content, re.S)      # 不加re.S会匹配失败（re.S: 使'.'会匹配换行符）
print(res.group(1))
'''
re.I: 大小写不敏感
re.L: 做本地化识别匹配
re.M: 多行匹配，影响^,$
re.S: 使.匹配换行符
re.U: 根据unicode解析字符
re.X: 更灵活的格式
'''

print('--------------------------------')

# 转义匹配 加'\'

