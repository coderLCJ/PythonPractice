from lxml import etree
text = '''
<div>
<ul>
<li class="item-0 item-1" name="one"><a herf="link1.html">1 page</a></li>
<li class="item-0"><a herf="link1.html">2 page</a></li>
<li class="item-0"><a herf="link1.html">3 page</a></li>
<li class="item-0"><a herf="link1.html">4 page</a></li>
<li class="item-0"><a herf="link1.html">5 page</a>
</ul>
</div>
'''
html = etree.HTML(text)     # 自动修正HTML
res = etree.tostring(html)  # 此时输出结果为bytes类型
# print(res.decode('utf-8'))  # 利用decode方法转换为str类型

# print('------------------')
# # 也可以直接读取文件进行解析
# html = etree.parse('./test.html', etree.HTMLParser())
# res = etree.tostring(html)  # 此时输出结果为bytes类型
# print(res.decode('utf8'))  # 利用decode方法转换为str类型

res1 = html.xpath('//*')    # 选取所有节点
res2 = html.xpath('//li')   # 选取li节点
res3 = html.xpath('//li/a')   # 选取li节点的直接子节点a
res4 = html.xpath('//li//a')   # 选取li节点的所有子孙节点a
# //用于获取子孙节点 /用于获取直接子节点 .选取当前节点 ..选取当前节点的父节点
# @获取属性
print(res1)
print(res2)
print(res2[0])  # 结果为列表形式

# 注意三者的区别
res5 = html.xpath('//li[@class="item-0"]/text()')
print(res5)
res5 = html.xpath('//li[@class="item-0"]/a/text()')
print(res5)
res5 = html.xpath('//li[@class="item-0"]//text()')
print(res5)
# 属性多值匹配
res = html.xpath('//li[contains(@class, "item-0 item-1")]//text()')
print(res)
# 多属性匹配 用and连接
res = html.xpath('//li[contains(@class, "item-1") and @name="one"]//text()')
print(res)

# 按序选择节点
res = html.xpath('//li[1]/a/text()')    # 第一个li节点
print(res)
res = html.xpath('//li[last()]/a/text()')   # 最后一个li节点
print(res)
res = html.xpath('//li[position()<3]/a/text()')     # 序号小于3的li节点
print(res)

# 节点轴选择
res = html.xpath('//li[1]/ancestor::*')     # 获取祖先节点 ::后跟选择器 *选择所有祖先
print(res)
res = html.xpath('//li[1]/ancestor::div')     # 获取祖先节点 ::后跟选择器 *选择所有div祖先
print(res)
'''
attribute: 获取所有属性值
child: 获取所有直接子节点
descendant: 获取所有子孙节点
following: 获取当前节点之后的所有节点
following-sibling: 获取当前节点之后的所有兄弟节点
'''