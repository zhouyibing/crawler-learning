import csv
import os

import lxml.html
import requests

url = "https://www.moretickets.com/list/3101-concerts/hottest"
source = requests.get(url).content.decode('utf-8')
selector = lxml.html.fromstring(source)
item_list = selector.xpath('//div[@class="shows-container"]/a[@class="show-items sa_entrance"]')
csv_list = []
for item in item_list:
    detail = item.xpath('div/div/div[@class="show-detail"]')[0]
    detail_url = "https://www.moretickets.com"+item.xpath('@href')[0]
    title = detail.xpath('div[@class="show-name"]/text()')[0].strip()
    venue = detail.xpath('div[@class="row-wrapper bottom-align"]/div[@class="show-addr"]/text()')[0].strip()
    time = detail.xpath('div[@class="row-wrapper bottom-align"]/div[@class="show-time"]/text()')[0].strip()
    price_item = detail.xpath('div[@class="row-wrapper bottom-align"]/div[@class="show-price"]')[0]
    price = price_item.xpath('text()')[0].strip() + price_item.xpath('span[@class="price-unit"]/text()')[0].strip()
    tags = detail.xpath('div[@class="tags"]')[0].xpath('string(.)').strip()

    item_dict = {'title': title, 'detail_url': detail_url, 'venue': venue, 'time': time,
                 'price': price, 'tags': tags}
    print(item_dict)
    csv_list.append(item_dict)

path = 'C:\\Users\\ASUS\\Pictures\\crawler\\ch5'
os.makedirs(path, exist_ok=True)
with open(os.path.join(path, 'damai.csv'), 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['title', 'detail_url', 'venue', 'time', 'price', 'tags'])
    writer.writeheader()
    writer.writerows(csv_list)
print('done')

