import json
# loads(): 将JSON文本字符串转换为JSON对象
# dumps(): 将JSON对象转换为JSON字符串

Str = '''
[{
    "name": "laity",
    "gender": "male",
    "birthday": "1999-8-6"
}, {
    "name": "cj",
    "gender": "female",
    "birthday": "1999-1-1"
}]
'''
# 需要注意 JSON必须用双引号

# 读取JSON
print(type(Str))
data = json.loads(Str)
print(data)
print(type(data))
print(data[0]['name'])
print(data[0].get('name'))  # 效果同上
print(data[0].get('age'))   # 推荐使用get 找不到属性不会报错
print(data[0].get('age', 'Laity——J')) # 找不到该键名 则会返回第二个参数

with open('data2.json', 'r') as file:
    Str = file.read()
    data = json.loads(Str)
    print(data)

print('='*80)

# 输出JSON
data = [{
    'name': '张三',
    'gender': 'male',
    'birthday': '1999-8-6'
}]
Json = json.dumps(data, indent=2, ensure_ascii=False)   # indent: 缩进字符个数
# 这是因为json.dumps 序列化时对中文默认使用的ascii编码.想输出真正的中文需要指定ensure_ascii=False
print(Json)
with open('data3.json', 'w', encoding='utf8') as file:  # 指定编码 否则中文会乱码
    file.write(Json)

