import requests, re

res = requests.get('https://y.qq.com/n/yqq/toplist/4.html')
res.encoding = res.apparent_encoding
f = open('spider.txt', 'a', encoding='utf-8')
s = re.findall('class="toplist_nav__link">(.*?)</a>', res.text)
for i in s:
    f.write(i + '\n')
f.close()
