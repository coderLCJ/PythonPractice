# -*- coding: utf-8 -*-
from lxml import etree
text = '''
<div>
<ul>
<li class="item-0 item-1" name="one"><a herf="link1.html">0 page</a></li>
<li class="item-0"><a herf="link1.html">1 page</a></li>
<li class="item-0"><a herf="link1.html">2 page</a></li>
<li class="item-0"><a herf="link1.html">3 page</a></li>
<li class="item-0"><a herf="link1.html">4 page</a>
</ul>
</div>
'''
html = etree.HTML(text)  # 自动修正HTML
res = html.xpath('//li[@class="item-0"]/a/text()')
print(res)
f = open('data.txt', 'w')
for s in res:
    f.write(s + '\n')

