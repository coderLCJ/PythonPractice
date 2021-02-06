import requests
import re
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
    # 浏览器标识 不加的话无法爬取
}
r = requests.get('https://www.zhihu.com/explore', headers=headers)
pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)   # 该正则表达式不正确
titles = re.findall(pattern, r.text)
print(titles)
s = open('html.txt', 'w', encoding='utf8')
s.write(r.text)
s.close()
