import json


def request(flow):
    request = flow.request
    print(f'请求的url:{request.url}')
    print(f'请求方式:{request.method}')
    print(f'请求的Cookie:>>>{request.cookies}<<<')
    print(f'请求的body:{request.text}')


def response(flow):
    req = flow.request
    resp = flow.response
    if 'baidu.com' in req.url:
        print('命中了baidu.com的请求')
        print(f'请求的url:{req.url}')
        print(f'请求参数:{req.query}')
        print(f'请求的headers:{req.headers}')
        print(f'响应的headers:{resp.headers}')
        print(f'响应的body:{json.loads(resp.content)}')