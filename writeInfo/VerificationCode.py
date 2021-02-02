from selenium import webdriver
import time
from PIL import Image
import tesserocr

base_url = 'http://xgb.ahstu.edu.cn/SPCP/Web'
browser = webdriver.Chrome()
browser.maximize_window()
browser.implicitly_wait(10)
browser.get(base_url)
# (1)登录页面截图
browser.save_screenshot('F:/MyGithubFile/python/writeInfo/full.png')     # 可以修改保存地址
# (2)基操
# browser.find_element_by_name("username").send_keys("gxx")
# browser.find_element_by_name("password").send_keys("123456")
# time.sleep(2)
# (3)获取图片验证码坐标
code_ele = browser.find_element_by_class_name('code-img')
print("验证码的坐标为：", code_ele.location)    # 控制台查看{'x': 1086, 'y': 368}
print("验证码的大小为：", code_ele.size)    # 图片大小{'height': 40, 'width': 110}
# (4)图片4个点的坐标位置

left = 1098   # x点的坐标
top = 343    # y点的坐标
right = 80 + left  # 上面右边点的坐标
down = 25 + top  # 下面右边点的坐标
image = Image.open('full.png')
# (4)将图片验证码截取
code_image = image.crop((left, top, right, down))
code_image.save('F:/MyGithubFile/python/writeInfo/code.png')     # 截取的验证码图片保存为新的文件
print(tesserocr.image_to_text(Image.open('F:/MyGithubFile/python/writeInfo/code.png')))

