import re
import sys
import redis

redisCli = redis.StrictRedis()
print('start')
for line in sys.stdin:
    print(line)
    cookie = re.search('>>>(.*?)<<<', line)
    if cookie:
        print(cookie.group(1))
        redisCli.set('cookie', cookie.group(1))

print('end')