import requests
from utils.LogUtil import my_log


# 重构
class Request:
    def __init__(self):
        self.log = my_log("Requests")

    def requests_api(self, url, data=None, json=None, headers=None, cookies=None, allow_redirects=None, method='get'):
        if method == "get":
            self.log.debug("发送get请求")
            r = requests.get(url, data=data, json=json,  headers=headers, cookies=cookies)
        elif method == "post":
            self.log.debug("发送post请求")
            r = requests.post(url, data=data, json=json,  headers=headers, cookies=cookies, allow_redirects=allow_redirects)
        elif method == "put":
            self.log.debug("发送put请求")
            r = requests.put(url, data=data, json=json,  headers=headers, cookies=cookies)
            # 获取响应的内容
        code = r.status_code
        headers = r.headers
        try:
            body = r.json()
        except Exception as e:
            body = r.text
        # 内容存到字典
        res = dict()
        res["code"] = code
        res["headers"] = headers
        res["body"] = body
        # 字典返回
        return res

    def get(self, url, **kwargs):
        return self.requests_api(url, method='get', **kwargs)

    def post(self, url, **kwargs):
        return self.requests_api(url, method='post', **kwargs)

    def put(self, url, **kwargs):
        return self.requests_api(url, method='put', **kwargs)
