import json

import requests
import re

class LetvSpider(object):
    COMMENT_URL = 'https://api-my.le.com/vcm/api/list?jsonp=jQuery191004864255188153055_1714918190742&type=video&rows=20&page=1&sort=&cid=2&source=1&xid={xid}&pid={pid}&ctype=cmt%2Cimg%2Cvote&listType=1&_=1714918190756'
    HEADERS = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Cookie': 'tj_lc=2b25f9c4924b8d2c90cbf0bd36496efb; tj_uuid=-_17149175275392574892; tj_env=1; bd_xid=2b25f9c4924b8d2c90cbf0bd36496efb; language=zh-cn; sso_curr_country=CN; currentLeft_miniPlayer=1019; currentTop_miniPlayer=-15; tj_v2c=-30744694_2-25953200_2-1611859_2-77541041_2-77538325_1009; ark_uuid=ck-4ca8014d-34ce-4e7a-ad73-c44bc18cbead-0505-220952',
        'Host': 'api-my.le.com',
        'Pragma': 'no-cache',
        'Referer': 'https://www.le.com/',
        'Sec-Fetch-Dest': 'script',
        'Sec-Fetch-Mode': 'no-cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'sec-ch-ua': 'Chromium;v="124",Google Chrome;v="124", Not-A.Brand;v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': 'Windows'
    }

    def __init__(self, url):
        self.url = url
        self.necessary_info = {}
        self.get_necessary_id()
        self.get_comment()

    def get_source(self, url, headers):
        return requests.get(url, headers=headers).content.decode('utf-8')

    def get_necessary_id(self):
        source = self.get_source(self.url, {})
        vid = re.search('vid: (\\d+)', source).group(1)
        pid = re.search('pid: (\\d+)', source).group(1)
        self.necessary_info['vid'] = vid
        self.necessary_info['pid'] = pid

    def get_comment(self):
        comment_url = self.COMMENT_URL.format(xid=self.necessary_info['vid'], pid=self.necessary_info['pid'])
        comment_source = self.get_source(comment_url, self.HEADERS)
        source_json = comment_source[comment_source.find('{"'): -1]
        comment_dict = json.loads(source_json)
        comments = comment_dict['data']
        for comment in comments:
            print(f'发帖人：{comment["user"]["username"]}，评论内容：{comment["content"]}')


if __name__ == '__main__':
    spider = LetvSpider('https://www.le.com/ptv/vplay/30744694.html?ref=index_focus_1')