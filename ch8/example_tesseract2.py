import lxml.html
import pytesseract
import requests
from PIL import Image
import base64
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# image = Image.open('img.png')
# text = pytesseract.image_to_string(image)
# print(text)
login_url = 'https://www.baidu.com/hrss-pw-ui-hunan/#/login'
service = Service(executable_path=r'C:\softwares\chromedriver\chromedriver.exe')

chrome_options = Options()
# 创建WebDriver
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get(login_url)
img = driver.find_element(By.XPATH, '//div[@class="el-input-group__append"]/img')
img_src = img.get_attribute('src')
print(img_src)
# 去掉base64编码头部
img_src = img_src.replace('data:image/png;base64,', '')
image_data = base64.b64decode(img_src)
with open('img.png', 'wb') as f:
    f.write(image_data)

image = Image.open('img.png')
# 用pytesseract识别图片中的文字
text = pytesseract.image_to_string(image)
print(text)
