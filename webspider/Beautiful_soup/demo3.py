html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>The Laity's story</title>
</head>
<body>
    <ul><li id="list-1" name="1">1</li></ul>
    <ul><li id="list-2">2</li></ul>
    <ul><li id="list-3">3</li></ul>
    <ul><li id="list-4">4</li></ul>
    <ul><li id="list-5">5</li></ul>
    <ul><li id="list-6">6</li></ul>
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
import re

soup = BeautifulSoup(html, 'lxml')
# CSS选择器 使用select()方法
print(soup.select('body .title'))
print(soup.select('p a'))

# 嵌套查询 获取属性
for i in soup.select('ul'):
    for j in i.select('li'):
        print(j['id'])

# 获取文本 除了string 也可以用get_text()方法
for i in soup.select('ul'):
    for j in i.select('li'):
        print(j.string)
        print(j.get_text())
        # 结果一致
