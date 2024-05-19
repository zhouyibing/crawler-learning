import os
from functools import partial

import requests
import re
from multiprocessing.dummy import Pool


def get_chapter_url(root_path, index_path):
    """
    获取所有章节的url
    :param index_path: 首页url
    :return: 各章节url
    """
    chapter_url = []
    html = requests.get(root_path+index_path).content.decode('utf-8')
    tbody = re.findall('<ul class="chapter">(.*?)</ul>+', html, re.S)[0]
    hrefs = re.findall('href="(.*?)"', tbody)
    for href in hrefs:
        chapter_url.append(root_path + href)
    return chapter_url


def get_chapter_content(chapter_url):
    """
    获取章节内容
    :param chapter_url: 章节url
    :return: 章节名,内容
    """
    html = requests.get(chapter_url).content.decode('utf-8')
    charter_name = re.search('<h1 class="title">(.*?)<', html, re.S)
    if charter_name:
        charter_name = charter_name.group(1)  # 获取章节名
    else:
        # 无法匹配，打印url和html
        print("无法匹配章节名：{},内容：{}".format(chapter_url, html))
        return None, None
    content = re.search('<div id="text"><p>(.*?)</p>', html, re.S).group(1)  # 获取章节内容
    # 替换<br />
    content = content.replace('<br/>', '\n')
    return charter_name, content


def save(save_dir, chapter_name, content):
    """
    保存章节内容
    :param save_dir: 保存路径
    :param chapter_name: 章节名
    :param content: 章节内容
    :return:
    """
    os.makedirs(save_dir, exist_ok=True)
    with open(os.path.join(save_dir, chapter_name + '.txt'), 'w', encoding='utf-8') as f:
        f.write(content)


def fetch_chapter(save_dir, chapter_url):
    """
    获取章节内容并保存
    :param save_dir: 保存路径
    :param chapter_url: 章节url
    :return:
    """
    chapter_name, content = get_chapter_content(chapter_url)
    if chapter_name and content:
        save(save_dir, chapter_name, content)


if __name__ == '__main__':
    host = "https://m.xiaoshuopu.com"
    root_path = "/xiaoshuo/29/29467/"
    save_dir = 'C:\\Users\\ASUS\\Pictures\\crawler\\ch4\\完美世界'
    chapter_urls = get_chapter_url(host, root_path)
    pool = Pool(5)
    partial_fetch_chapter = partial(fetch_chapter, save_dir)
    pool.map(partial_fetch_chapter, chapter_urls)
    # args = [(save_dir, url) for url in chapter_urls]
    # pool.starmap(fetch_chapter, args)
