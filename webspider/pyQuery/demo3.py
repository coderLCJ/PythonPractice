html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>The Laity's story</title>
</head>
<body>
    <div class="t1">
        <div class="wrap" id="wrap_">
                <li id="list-1" name="1" class="l1"><b>1</b><p> Hello World</p></li>
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
a = doc('.t1 .wrap')
print(a.attr('id')) # 当包含多个属性时 只输出第一个 若要全部输出则需要遍历
print(a.attr.id)    # 效果同上

a = doc('li')
print(a)
print(a.html())     # 返回第一个li节点内部的HTML文本
print(a.text())     # 返回所有li节点内部的纯文本 不需遍历

# 动态修改类属性
li = doc('.wrap #list-1')
print(li)
li.removeClass('l1')
print(li)
li.add_class('new_l1')
print(li)

# 修改其他属性
li.attr('id', 'new_list-1') # 将id修改为new_list-1
print(li)
li.text('new 1')
print(li)
li.html('<a>1</a>')
print(li)

# remove,append,empty,prepend
doc = pq(html)
p = doc('.wrap #list-1')
print(p.text())
p.find('b').remove()    # 删除b标签 只输出p标签内的内容
print(p.text())

# 伪类选择器
li = doc('li')
print(doc('li:first-child'))
print(doc('li:last-child'))
print(doc('li:nth-child(2)'))
