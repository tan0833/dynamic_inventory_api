import unittest,ddt
from common.replace_opertate import ReplaceOperte
from config.Log import Log
from config.get_conf import Conf
from util.operate_excel import Operate_excel
from runMain.run_main import RunMain
from util.operate_global import GlobalDict

#定义全局字典
temp_dict = {}

res = Operate_excel(Conf().get_file_path('data','测试接口.xlsx'),"登录")
login = res.excel_dict()

r = Operate_excel(Conf().get_file_path('data','测试接口.xlsx'),"动态库存")
d = r.excel_dict()

@ddt.ddt
class TestRunMain(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.conf = Conf()
        cls.log = Log()
        cls.request_url = cls.conf.get_value('request_url','url')
        cls.service = cls.conf.get_value('service','dynamic')
        cls.ro = ReplaceOperte(temp_dict)
        cls.run_main = RunMain()


    @ddt.data(*login)
    def test_login(self,data):
        '''
        测试登录
        :param data:
        :return:
        '''
        method = data['method']
        url = self.request_url  + self.ro.replace_excel(data['path'])

        header = data['header']
        header = self.ro.replace_excel(header)
        if header.startswith('{'):
            header = eval(header)

        params = data['params']
        params = self.ro.replace_excel(params)
        if params.startswith('{'):
            params = eval(params)

        global_value = data['global']
        if global_value.startswith('{'):
            global_value = eval(global_value)

        result = self.run_main.run_main(method, url=url, data=params, header=header)
        self.ro.replace_global_value(global_value,result)

    @ddt.data(*d)
    def test_run_mai(self,data):
        method = data['method']
        url = self.request_url + self.service + self.ro.replace_excel(data['path'])

        header = data['header']
        header = self.ro.replace_excel(header)
        if header.startswith('{'):
            header = eval(header)

        params = data['params']
        params = self.ro.replace_excel(params)
        if params.startswith('{'):
            params = eval(params)

        global_value = data['global']
        if global_value.startswith('{'):
            global_value = eval(global_value)

        result = self.run_main.run_main(method, url=url, data=params, header=header)
        self.ro.replace_global_value(global_value, result)

if __name__ == '__main__':
    unittest.main()