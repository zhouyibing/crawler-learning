import lxml.html
import pytesseract
import requests
from PIL import Image
import base64
# image = Image.open('img.png')
# text = pytesseract.image_to_string(image)
# print(text)
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Length': '32',
    'Content-Type': 'application/json',
    'Cookie': '__jsluid_s=2608f0386dc53f1e6821e377d9d05b63',
    'Host': 'www.baidu.com',
    'Origin': 'https://www.baidu.com',
    'Pragma': 'no-cache',
    'Referer': 'https://www.baidu.com/hrss-pw-ui-hunan/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'channel': '1',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sessionAppName': 'apptest'
}
login_url = 'https://www.baidu.com/hrss-pw-ui-hunan/#/login'
session = requests.Session()
html = session.get(login_url, headers=headers).content.decode()
selector = lxml.html.fromstring(html)
img_base64 = selector.xpath('//div[@class="el-input-group__append"]/img/@src')
image_data = base64.b64decode(img_base64[0])
# 用pytesseract识别图片中的文字
text = pytesseract.image_to_string(image_data)
print(text)

# 使用PIL库读取图片
image = Image.open(img_bytes)
