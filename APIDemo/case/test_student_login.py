import unittest
import requests
from lib.mode_lib import set_pwd
from ddt import ddt,data,unpack,file_data
from setting import *

@ddt
class Student_loginTest(unittest.TestCase):
    @file_data(os.path.join(DATA_PATH, 'student_login.yaml'))
    def test_student_login(self, **args):
        #获取参数
        url = args.get('url')
        data = args.get('data')
        assertInfo = args.get("assertInfo")

        # 密码加密
        if 'password' in data:
            data['password'] = set_pwd(data['password'])

        #发送请求
        result = requests.post(url=url, json=data)
        #结果处理
        rest = result.text  #字符串
        rest = rest.replace('":"', '=').replace('":','=')
        for check in assertInfo:
            self.assertIn(check, rest)


if __name__ == '__main__':
    unittest.main()
