import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
# 如果chromedriver在系统路径中，可以直接使用
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

service = Service(executable_path=r'C:\softwares\chromedriver\chromedriver.exe')

chrome_options = Options()
# chrome_options.add_argument("--headless")  # 如果需要无头模式

# 创建WebDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

# driver = webdriver.Chrome(r'C:\softwares\chromedriver\chromedriver.exe')
driver.get('http://exercise.kingname.info/exercise_advanced_ajax.html')
# wait 5s
# time.sleep(5)
# 智能的等待加载完成
try:
    # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "content")))
    WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "content"), '通关'))
except Exception as e:
    print('加载失败')
    print(e)

# 获取页面源码
html = driver.page_source
print("html={}".format(html))

# 提取页面元素
# content = driver.find_element_by_id("content")
# contentDiv = driver.find_element_by_xpath('//div[@class="content"]')
# contentDiv = driver.find_element(By.XPATH, '//div[@class="content"]')
contentDiv = driver.find_element(By.CLASS_NAME, 'content')
print("context text={}".format(contentDiv.text))

driver.quit()
