import requests

r = requests.get('https://www.zhihu.com')
print(r.cookies)
for key, value in r.cookies.items():
    print('key = ' + key + ', value = ' + value)


# 利用cookies维持登录状态
headers = {
    'Cookie': '_zap=3b8a76c1-f356-42e3-8e0e-64a0bd4f0ee2; d_c0="ACCcc17ycBKPTr6-L1WUgVS00EquRWZUZyM=|1609597373"; _xsrf=liidVJt5ybJV7xMXXRiP5UWS1szzkD45; captcha_session_v2="2|1:0|10:1612403282|18:captcha_session_v2|28:YzBkbDRrZ2VlcnVrNTRoMmU1ODA=|aa9fb6cdca1121306fd2d654d52689023e23626def1ada9e339a752f252dbb18"; r_cap_id="ZGFmODViZmUwMjI2NDM3ZDlmZjQ3MjkyMTc2NGYzNmI=|1612403285|b5d38c5fbc442e867f6c468301e78a8ed6f81c67"; cap_id="MTEyNjFmMTBjMGEwNDU3MGFmMjBiMDk5MWNlODgwMTg=|1612403285|d1fa5aedac22061d65a481443a6812f19373002f"; l_cap_id="ZjkwYWMyODI2Y2I4NDNkMzliZjJiMzU1ZmJjNzJmZjc=|1612403285|1691ae43e98cf579ee57cdf4c497bd21228ff89e"; z_c0=Mi4xUkRLaUJnQUFBQUFBSUp4elh2SndFaGNBQUFCaEFsVk5lYUFJWVFEeEZOYzNrUEtCMHI5NVI4ZnFxR2VlamN1NTRB|1612403321|14eb9cd6f819bfe8cce98014dad422609ecd6cd7; tst=r; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1612444354,1612577642,1612698546,1612705049; SESSIONID=CfWJtYFpliFznwcST386FRecAgDnAJX8XyxjhWQn4IK; JOID=UlkcA0lzvt-I2jX3OHP9Tz_9CGMjMdCBwKxtuUEd1pH7tkCVY2JSy-jZPPYzAirdpj9D6eyv9lbH0a_F1wqzHG0=; osd=Wl0WA0N7utWI0D3zMnP3Rzv3CGkrNdqByqRps0EX3pXxtkqdZ2hSweDdNvY5Ci7XpjVL7eav_F7D26_P3w65HGc=; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1612705240; KLBRSID=c450def82e5863a200934bb67541d696|1612705239|1612705045',
    'Host': 'www.zhihu.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
h = {
    'Host': 'www.zhihu.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}

p = requests.get('https://www.zhihu.com', headers=headers)
k = requests.get('https://www.zhihu.com', headers=h)

fp1 = open('my_zhihu1.txt', 'w', encoding='utf-8')
fp2 = open('my_zhihu2.txt', 'w', encoding='utf-8')
fp1.write(p.text)
fp2.write(k.text)

