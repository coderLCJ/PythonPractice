from pyquery import PyQuery as pq
import requests

headers = {
    'Cookie': '_zap=3b8a76c1-f356-42e3-8e0e-64a0bd4f0ee2; d_c0="ACCcc17ycBKPTr6-L1WUgVS00EquRWZUZyM=|1609597373"; _xsrf=liidVJt5ybJV7xMXXRiP5UWS1szzkD45; captcha_session_v2="2|1:0|10:1612403282|18:captcha_session_v2|28:YzBkbDRrZ2VlcnVrNTRoMmU1ODA=|aa9fb6cdca1121306fd2d654d52689023e23626def1ada9e339a752f252dbb18"; r_cap_id="ZGFmODViZmUwMjI2NDM3ZDlmZjQ3MjkyMTc2NGYzNmI=|1612403285|b5d38c5fbc442e867f6c468301e78a8ed6f81c67"; cap_id="MTEyNjFmMTBjMGEwNDU3MGFmMjBiMDk5MWNlODgwMTg=|1612403285|d1fa5aedac22061d65a481443a6812f19373002f"; l_cap_id="ZjkwYWMyODI2Y2I4NDNkMzliZjJiMzU1ZmJjNzJmZjc=|1612403285|1691ae43e98cf579ee57cdf4c497bd21228ff89e"; z_c0=Mi4xUkRLaUJnQUFBQUFBSUp4elh2SndFaGNBQUFCaEFsVk5lYUFJWVFEeEZOYzNrUEtCMHI5NVI4ZnFxR2VlamN1NTRB|1612403321|14eb9cd6f819bfe8cce98014dad422609ecd6cd7; tst=r; q_c1=49d23a46a46d4772b417b077ff1b9782|1612745594000|1612745594000; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1612853676,1612853917,1612926641,1613614082; SESSIONID=8TqEXoypdEyVctjtPFmXmlUWWl8EIYiqO1yHJf40XNS; JOID=VV0cBkju0BwgxL7zfeyWi5bigWJh1IhhY5jThgGOl2l6oc6bBeAcO0LCsPN3ZIVBnIifLhBg_OaIjI1szmTqQw0=; osd=VlgUBkvt1RQgx732deyViJPqgWFi0YBhYJvWjgGNlGxyoc2YAOgcOEHHuPN0Z4BJnIucKxhg_-WNhI1vzWHiQw4=; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1613614224; KLBRSID=4efa8d1879cb42f8c5b48fe9f8d37c16|1613614222|1613614076',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
}

res = requests.get('https://www.zhihu.com/hot', headers=headers)
html = res.text
doc = pq(html)
items = doc('.HotItem-content').items()
ques = open('question.txt', 'w', encoding='utf-8')
ans = open('answer.txt', 'w', encoding='utf-8')
for i in items:
    title = i('a').attr('title')
    ques.write(title + '\n'*2)    # 写入问题
    ans_href = i('a').attr('href')
    ans_doc = pq(requests.get(ans_href, headers=headers).text)
    ans_items = ans_doc('.List-item').items()
    for it in ans_items:
        ans_author = it('meta:first-child').attr('content')
        ques.write('作者：' + ans_author + '\n')
        print(ans_author)
        ans_text = it('.RichContent-inner').text()
        print(ans_text)
        ques.write(ans_text + '\n' + '-'*50 + '\n')
    ques.write('#'*50 + '\n')


ques.close()
ans.close()

