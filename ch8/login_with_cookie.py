import requests

HEADERS = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Content-Length': '130',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': "wordpress_sec_957d633a49ff6485cdc9156ef19b311a=zhouyibing%7C1715265601%7C6hDqgbFhkLiskYyzmPyzp3nVCeDWVv4ZeRwF7t9aeOG%7C2fadeee0fafb29f2b22f3efb583d8aa6e4c8bc9de1895821041e32c4c2cefdc1; __gads=ID=5f9059b34d9ec8d0':T=1715092298':RT=1715092298':S=ALNI_MZpvkqA7ncqiHjZqix-CKkiUaqFPg; __gpi=UID=00000e118edc601e':T=1715092298':RT=1715092298':S=ALNI_MYt9XiEYRNIUmjfk2SU2lOk7abngw; __eoi=ID=7c28483a4f6d08f4':T=1715092298':RT=1715092298':S=AA-AfjYKVXmONyz_ASgKf5KGELk-; wordpress_test_cookie=WP%20Cookie%20check; wp_lang=zh_CN; wordpress_logged_in_957d633a49ff6485cdc9156ef19b311a=zhouyibing%7C1715265601%7C6hDqgbFhkLiskYyzmPyzp3nVCeDWVv4ZeRwF7t9aeOG%7C03fc21720712b4d311078cfab3d354e34a40ea2403082e3d36e1384a0e716a6d; wp-settings-7248=mfold%3Do%26wplink%3D1%26libraryContent%3Dbrowse; wp-settings-time-7248=1715092803",
        'Origin': 'https://ifeve.com',
        'Pragma': 'no-cache',
        'Priority': 'u=1, i',
        'Referer': 'https://ifeve.com/wp-admin/edit.php?post_type=post',
        'Sec-Ch-Ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }

session = requests.Session()
source = session.get('https://ifeve.com/wp-admin/', headers=HEADERS).content.decode()
print(source)
