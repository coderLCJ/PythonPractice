html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>The Laity's story</title>
</head>
<body>
    <p class="title" name="laity"><b>The Laity's story</b></p>
    <p class="story">
        Once upon a time there were three little sisters; and their names were:
        <a href="http://example.com/one" class="sister" id="link1"><!-- Elsie --></a>
        <a href="http://example.com/two" class="sister" id="link2">Lacie</a>and
        <a href="http://example.com/three" class="sister" id="link3">Tillie</a>;
        and they lived at the bottom of a well.
    </p>
    <p class="story">....</p>
'''
from bs4 import BeautifulSoup

soup = BeautifulSoup(html, 'lxml')  # 初始化BeautifulSoup 此时已将html文档补全
print(soup.prettify())      # 以标准的缩进格式输出字符串
print(soup.title.string)    # title方法获取title节点 string属性获取节点内容
print(soup.p)   # 只会匹配第一个p标签
print(soup.title.name)  # 获取节点名称
print(soup.p.attrs)     # 获取节点属性
print(soup.p.attrs['name'])     # 指定属性
print(soup.p['name'])           # 效果同上
print(soup.p['class'])          # class不唯一 返回的是字符串列表；name唯一 返回的是字符串 这点需要注意

# 支持嵌套选择
print(soup.head.title.string)

# 关联选择
print(soup.p.contents)  # 获取所有直接子节点 返回列表
for num, child in enumerate(soup.body.children):    # children返回生成器（也是直接子节点） 用for遍历输出结果
    print(num, child)
# enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标

print(list(soup.body.children)[1])      # 返回的是生成器 转换为list即可输出其内容
print(list(soup.body.children)[1].string)

# descendants：返回所有子孙节点生成器
print(soup.a.parent)
# parent：获取直接父节点所有内容
# parents： 获取所有的祖先内容
'''
next_sibling: 获取节点的下一个兄弟节点
previous_sibling: 获取节点的上一个兄弟节点
next_siblings: 获取节点后面的所有兄弟节点
previous_siblings: 获取节点前面的所有兄弟节点
'''

