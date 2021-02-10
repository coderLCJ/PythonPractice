import re


content = 'Hello 123 4567 World_This is a Regex Demo'
pattern = '^Hello\s\d\d\d\s\d{4}\s\w{10}'   # 将正则表达式编译为正则表达式对象, 也可以传入r.S等修饰符, 这样在匹配时就可以不用加
res = re.match(pattern, content)
print(res.group())      # 输出匹配内容
print(res.span())       # 输出匹配范围
