import unittest
from request_obj import BaseRequestObj

class TestZKScore(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        print('开始测试----')
        self.req_obj = BaseRequestObj()
        self.host_name = 'https://myyz.yzsmk.net'

    @classmethod
    def tearDownClass(self):
        print('结束测试----')



    def test_public_test_params(self):
        """
        中考成绩查询
        :return:
        """
        res = self.req_obj.get_request(self.host_name + '/exam/v1/ZKScore', {'xm': '巫丹妮', 'zkzh': 1907010102,'pwd':'zch999999'})
        status_code = res.status_code
        #res_data = res.json()
        self.assertEqual(status_code, 200)
        #self.assertEqual(res_data.get('errorCode'), 0)
        print('状态码:',res.status_code)
        print('响应信息:',res.json())

if __name__ == '__main__':
    unittest.main(verbosity=2)

