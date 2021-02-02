from selenium import webdriver
from PIL import Image
from email.mime.text import MIMEText
from email.header import Header
import time, smtplib, tesserocr, selenium
import sys
print(sys.path)
# 打开chrome浏览器
driver = webdriver.Chrome()
# 进入健康情况填报官网
url = r'http://xgb.ahstu.edu.cn/SPCP/Web'
driver.get(url)
# 最大化窗口
driver.maximize_window()


# 点击体温
# driver.find_element_by_id('platform1').click()

# 登录信息
username = driver.find_element_by_xpath('//*[@id="StudentId"]')
stu_number = '2704170205'
username.send_keys(stu_number)
stu_password = '061773'
password = driver.find_element_by_xpath('//*[@id="Name"]')
password.send_keys(stu_password)


# 获取验证码 有时候会验证错误 重复验证直至进入页面
while True:
    try:
        driver.find_element_by_xpath('//*[@id="platfrom1"]/a/img')  # 尝试获取填体温页面 成功即登录成功
        break
    except:
        # 验证码错误 点击刷新一下
        driver.find_element_by_xpath('//*[@id="code-box"]').click()
        driver.save_screenshot('F:/MyGithubFile/python/writeInfo/full.png')  # 可以修改保存地址
        code_ele = driver.find_element_by_class_name('code-img')
        print("验证码的坐标为：", code_ele.location)  # 控制台查看{'x': 1086, 'y': 368}
        print("验证码的大小为：", code_ele.size)  # 图片大小{'height': 40, 'width': 110}
        # (4)图片4个点的坐标位置

        left = 1098  # x点的坐标
        top = 343  # y点的坐标
        right = 80 + left  # 上面右边点的坐标
        down = 25 + top  # 下面右边点的坐标
        image = Image.open('full.png')
        # (4)将图片验证码截取
        code_image = image.crop((left, top, right, down))
        code_image.save('F:/MyGithubFile/python/writeInfo/code.png')  # 截取的验证码图片保存为新的文件
        v_code = tesserocr.image_to_text(Image.open('F:/MyGithubFile/python/writeInfo/code.png'))
        print('验证码是:', v_code)
        code = driver.find_element_by_xpath('//*[@id="codeInput"]')
        code.send_keys(v_code)
        print('即将尝试登录....')
        driver.find_element_by_xpath('//*[@id="Submit"]').click()

# test
try:
    driver.find_element_by_xpath('//*[@id="platfrom2"]').click()

    # 填写成功
except:
    # 填写失败
    print('填写失败')
# --------------------------------------------------------------------------

# # 点击登录
# driver.find_element_by_class_name('submit_button').click()
# time.sleep(1)
# # 点击健康登记
# driver.find_element_by_partial_link_text('健康登记').click()

# 因为西工大会自动记录上一天的信息，所以不需要填报其他信息可直接提交
'''
#如果需要更改一些内容可参考以下代码
# 当前所在位置
driver.find_element_by_xpath('//*[@id="rbxx_div"]/div[3]/label[3]').click()

# 由于本人选取的国内，所有还有省市区的选择
driver.find_element_by_xpath('//*[@id="province"]/option[18]').click()
driver.find_element_by_xpath('//*[@id="city"]/option[4]').click()
driver.find_element_by_xpath('//*[@id="district"]/option[4]').click()

# 近15天是否前往或经停过武汉市、湖北省，或其他有病例报告的社区？
driver.find_element_by_xpath('//*[@id="rbxx_div"]/div[6]/label[3]').click()
driver.find_element_by_xpath('//*[@id="sfjthb_ms"]').clear()
driver.find_element_by_xpath('//*[@id="sfjthb_ms"]').send_keys('人在湖北')

# 近15天接触过出入或居住在武汉市、湖北省的人员，以及其它有病例社区的发热或呼吸道症状患者？
driver.find_element_by_xpath('//*[@id="rbxx_div"]/div[8]/label[3]').click()
driver.find_element_by_xpath('//*[@id="hbjry_ms"]').clear()
driver.find_element_by_xpath('//*[@id="hbjry_ms"]').send_keys('人在湖北')

# 近15天您或家属是否接触过疑似或确诊患者，或无症状感染患者（核酸检测阳性者）？
driver.find_element_by_xpath('//*[@id="rbxx_div"]/div[10]/label[1]').click()

# 今天的体温范围
driver.find_element_by_xpath('//*[@id="rbxx_div"]/div[12]/label[1]').click()

# 您或家属有无疑似症状?（可多选） 选择不上不明原因
driver.find_element_by_xpath('//*[@id="rbxx_div"]/div[14]/label[1]/div[1]').click()

# 您或家属当前健康状态
driver.find_element_by_xpath('//*[@id="rbxx_div"]/div[17]/label[1]').click()

# 您或家属是否正在隔离？（隔离是根据上级单位、医院相关要求的居家或封闭性隔离，宅在家的不属隔离）
driver.find_element_by_xpath('//*[@id="rbxx_div"]/div[20]/label[1]').click()
'''
# # 点击提交信息
# driver.find_element_by_partial_link_text('提交填报信息').click()
# time.sleep(1)
# # 郑重承诺
# driver.find_element_by_xpath('//*[@id="qrxx_div"]/div[2]/div[25]').click()
# # 确认提交
# driver.find_element_by_partial_link_text('确认提交').click()
# 关闭浏览器
# driver.close()

# --------------------------------------------------------------------------
# 发送邮件
# 发信方的信息：发信邮箱，QQ 邮箱授权码
# from_addr = '2907805535@qq.com'
# # 进入qq邮箱->设置->账户->找到stmp服务，点击开启。验证后会给你一个授权码，直接复制，填入下方即可
# password = 'xuejzktjljfsdhch'
#
# # 收信方邮箱
# to_addr = '2907805535@qq.com'
#
# # 发信服务器
# smtp_server = 'smtp.qq.com'
#
# # 邮箱正文内容，第一个参数为内容（正文部分），第二个参数为格式(plain 为纯文本)，第三个参数为编码
# msg = MIMEText('今日已经填报好健康信息', 'plain', 'utf-8')
#
# # 邮件头信息
# msg['From'] = Header(from_addr)
# msg['To'] = Header(to_addr)
# msg['Subject'] = Header('每日疫情填报情况')
#
# # 开启发信服务，这里使用的是加密传输
# server = smtplib.SMTP_SSL(smtp_server)
# server.connect(smtp_server, 465)
# # 登录发信邮箱
# server.login(from_addr, password)
# # 发送邮件
# server.sendmail(from_addr, to_addr, msg.as_string())
# # 关闭服务器
# server.quit()
