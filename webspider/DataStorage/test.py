html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>The Laity's story</title>
</head>
<body>
    <li id="list-1" name="1" class="t">1</li>
    <li id="list-2" class="t">2</li>
    <li id="list-3" class="t">3 <b class="q3"> 12</b> </li>
    <li id="list-4">4</li>
    <li id="list-5">5</li>
    <li id="list-6">6</li>
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

from pyquery import PyQuery as pq
import requests

# 取别名pq

# 传入文本
# doc = pq(html)
# print(doc('body .q3'))    # 传入CSS选择器 选择所有li节点
from icecream import ic

def test(n):
    print(n)
    return 2


n = 1
ic(test(n))
