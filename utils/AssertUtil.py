import json
from utils.LogUtil import my_log


# 定义封装类
class AssertUtil:
    # 初始化数据日志
    def __init__(self):
        self.log = my_log("AssertUtil")

    # code 相等
    def assert_code(self, code, expected_code):
        try:
            assert int(code) == int(expected_code)
            return True
        except:
            self.log.error('code error,code is s%,expected_code is s%'%(code, expected_code))
            raise
    # body相等

    def assert_body(self, body, expected_body):
        try:
            assert body == expected_body
            return True
        except:
            self.log.error('body error,body is s%,expected_body is s%'%(body, expected_body))
            raise

    # body包含
    def assert_in_body(self, body, expected_body):
        try:
            body = json.dump(body)
            assert expected_body in body
            return True
        except:
            self.log.error('not in body or body error,body is s%,expected_body is s%'%(body, expected_body))
            raise

    # header 包含
    def assert_in_header(self, header, expected_header):
        try:
            header = json.dump(header)
            assert expected_header in header
            return True
        except:
            self.log.error('not in header or header error,header is s%,expected_header is s%'%(header, expected_header))
            raise





