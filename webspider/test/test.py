import smtplib
from email.mime.text import MIMEText
from email.header import Header
# 发送给个人邮箱
# 用于构建邮件头cls

# 发信方的信息：发信邮箱，QQ 邮箱授权码
from_addr = '2907805535@qq.com'
# 进入qq邮箱->设置->账户->找到stmp服务，点击开启。验证后会给你一个授权码，直接复制，填入下方即可
password = 'xuejzktjljfsdhch'

# 收信方邮箱
to_addr = '2907805535@qq.com'

# 发信服务器
smtp_server = 'smtp.qq.com'

# 邮箱正文内容，第一个参数为内容（正文部分），第二个参数为格式(plain 为纯文本)，第三个参数为编码
msg = MIMEText('今日已经填报好健康信息', 'plain', 'utf-8')

# 邮件头信息
msg['From'] = Header(from_addr)
msg['To'] = Header(to_addr)
msg['Subject'] = Header('每日疫情填报情况')

# 开启发信服务，这里使用的是加密传输
server = smtplib.SMTP_SSL(smtp_server)
server.connect(smtp_server, 465)
# 登录发信邮箱
server.login(from_addr, password)
# 发送邮件
server.sendmail(from_addr, to_addr, msg.as_string())
# 关闭服务器
server.quit()
