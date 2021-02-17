html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>The Laity's story</title>
</head>
<body>
    <ul><li id="list-1" name="1">1</li></ul>
    <ul><li>2</li></ul>
    <ul><li>3</li></ul>
    <ul><li>4</li></ul>
    <ul><li>5</li></ul>
    <ul><li>6</li></ul>
    <p>this is a link</p>
    <p> link2 </p>
'''

from bs4 import BeautifulSoup
import re

soup = BeautifulSoup(html, 'lxml')
# find_all() 查询所有符合条件的元素
print(soup.find_all(name='ul'))     # 查询所有ul节点 返回列表类型
# 嵌套查询
for ul in soup.find_all(name='ul'):
    # print(ul)
    for li in ul.find_all(name='li'):
        print(li.string)    # 输出ul中的每个li的内容
# 传入attrs
print(soup.find_all(attrs={'id': 'list-1', 'name': '1'}))
# 常用属性可以不用attrs 如id class(写作class_)
print(soup.find_all(id='list-1'))   # 效果同上
# text 匹配节点的文本 可以传入字符串或者正则表达式
print(soup.find_all(text=re.compile('link')))
'''
其他用法
find() 只返回第一个匹配的元素
find_parent()
find_parents()
find_previous_siblings()
find_previous_sibling()
find_all_next()
find_next()
find_all_previous()
find_previous()
'''


