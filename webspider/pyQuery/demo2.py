html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>The Laity's story</title>
</head>
<body>
    <div class="t1">
        <div class="wrap">
                <li id="list-1" name="1" class="l1">1</li>
                <li id="list-2">2</li>
                <li id="list-3">3</li>
                <li id="list-4">4</li>
                <li id="list-5">5</li>
                <li id="list-6">6</li>
                <p class="title" name="laity"><b>The Laity's story</b></p>
                <p class="story">
                    Once upon a time there were three little sisters; and their names were:
                    <a href="http://example.com/one" class="sister" id="link1"><!-- Elsie --></a>
                    <a href="http://example.com/two" class="sister" id="link2">Lacie</a>and
                    <a href="http://example.com/three" class="sister" id="link3">Tillie<b class="sister"> tom</b></a>;
                    and they lived at the bottom of a well.
                </p>
                <p class="story">....</p>
        </div>
    </div>
'''

from pyquery import PyQuery as pq

doc = pq(html)
items = doc('.story')
# find查找所有子孙节点
print(items.find('.sister'))
# children只查找子节点
print(items.children('.sister'))

items = doc('b')
# parent获取直接父节点
print(items.parent())

print('-------------------------')

# parents获取所有祖先节点
items = doc('#list-1')
# print(items.parents())        # 输出所有祖先节点
print(items.parents('.wrap'))   # 只保留类属性为wrap的节点

# sibling获取兄弟节点
items = doc('.wrap #list-1')
print(items.siblings('li'))     # 选择所有li兄弟节点

# 遍历输出 调用items()方法
for li in items.siblings('li').items():
    print(li)
