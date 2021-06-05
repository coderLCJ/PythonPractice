# -*- coding: utf-8 -*-
import requests, re
from urllib.parse import urljoin

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Cookie': '__mta=244282938.1612941745358.1612951977410.1612951980170.28; _lxsdk_cuid=1778ad0cda9c8-0483a7549639ea-53e3566-144000-1778ad0cda9c8; uuid_n_v=v1; uuid=B844FC106B7011EB8804456773648793CA6BB710243C4F38939CF2FEA0D7C2B0; _csrf=12dd51af23d67f5284c6f9309b1273c6b7d35e20fdc4b0e4494bc765be89b365; _lxsdk=B844FC106B7011EB8804456773648793CA6BB710243C4F38939CF2FEA0D7C2B0; _lx_utm=utm_source=Baidu&utm_medium=organic; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1612941745,1612951312; __mta=244282938.1612941745358.1612951305703.1612951315086.17; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1612951980; _lxsdk_s=1778b5ee956-893-e03-c19||41',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
    'Host': 'maoyan.com'
}

f = open('html.txt', 'a')
url = 'https://maoyan.com/board/4?offset='
for i in range(6):
    url = urljoin(url, '?requestCode=6b4a15d594797c741183cfc83751d2cb1ft2j&offset=' + str(i * 10))
    print(url)
    res = requests.get(url, headers=headers)
    res.encoding = res.apparent_encoding
    f.write(res.text)
f.close()

f = open('html.txt', 'r')
fp = open('movie.txt', 'w')
text = f.read()
# 爬取标题
title_pat = '<meta name="keywords" content="(.*?)">'
# fp.write(res.text)
# fp.write(re.match(title_pat, res.text)[0] + '\n')
# print(res.text)
# 爬取榜单
board_id_pat = '.*{movieId:(\d+)}">(.*?)</a>'
board_star_pat = '<p class="star">(.*?)</p>'
board_time_pat = '<p class="releasetime">(.*?)</p>'

Id = re.findall(board_id_pat, text)
Star = re.findall(board_star_pat, text, re.S)
Time = re.findall(board_time_pat, text)
print(Star)

Len = len(Id)
for i in range(Len):
    fp.write('------------------------------------\n')
    fp.write('电影编号: ' + Id[i][0] + '\n')
    fp.write('电影名称: <<' + Id[i][1] + '>>\n')
    fp.write(Star[i].strip() + '\n')
    fp.write(Time[i] + '\n')

fp.close()
