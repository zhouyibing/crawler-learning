import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path=r'C:\softwares\chromedriver\chromedriver.exe')

chrome_options = Options()

# 创建WebDriver
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get('https://ifeve.com/wp-login.php')
# driver.get('https://www.zhihu.com/signin')

# 等待元素可点击
try:
    """account_login_tab = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//div[@class="SignFlow-tab" and contains(text(), "密码登录")]'))
    )
    # 点击元素
    account_login_tab.click()
    time.sleep(1)
    usernameInput = driver.find_element(By.NAME, 'username')
    usernameInput.clear()
    usernameInput.send_keys('15001917315')
    passwordInput = driver.find_element(By.NAME, 'password')
    passwordInput.clear()
    passwordInput.send_keys('zhou135678212')
    # 点击登录按钮
    login_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[@type="submit" and contains(text(), "登录")]'))
    )
    login_btn.click()"""
    usernameInput = driver.find_element(By.ID, 'user_login')
    usernameInput.clear()
    usernameInput.send_keys('zhouyibing')
    passwordInput = driver.find_element(By.ID, 'user_pass')
    passwordInput.clear()
    passwordInput.send_keys('135678212')

    # 点击登录按钮
    driver.find_element(By.ID, 'wp-submit').click()
    time.sleep(5)
    print(driver.page_source)
except Exception as e:
    print('加载失败')
    print(e)

driver.quit()
