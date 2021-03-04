from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import selenium
#  设置无界面模式
options = Options()
options.add_argument('-headless')
driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
print(driver.current_url)

