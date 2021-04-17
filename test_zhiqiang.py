import unittest
from request_obj import BaseRequestObj

class TestZhiQiang(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        print('开始测试----')
        self.req_obj = BaseRequestObj()
        self.host_name = 'http://139.196.95.147:3000'

    @classmethod
    def tearDownClass(self):
        print('结束测试----')



    def test_zhiqiang_test_params(self):
        """
        文玉测试
        :return:
        """
        res = self.req_obj.get_request(self.host_name )
        status_code = res.status_code
        # res_data = res.json()
        self.assertEqual(status_code, 200)
        #  print('状态码:',res.status_code)
        print('响应信息:',res.json())

if __name__ == '__main__':
    unittest.main(verbosity=2)

