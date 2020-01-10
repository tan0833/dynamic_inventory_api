import unittest,ddt,json,re
from common.replace_opertate import ReplaceOperte
from config.Log import Log
from config.get_conf import Conf
from util.operate_excel import Operate_excel
from runMain.run_main import RunMain
from util.operate_global import GlobalDict
from common.login import Login

r = Operate_excel(Conf().get_file_path('data','测试接口.xlsx'),0)
login = r.excel_dict()


@ddt.ddt
class TestRunMain(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.conf = Conf()
        cls.log = Log()
        cls.request_url = cls.conf.get_value('request_url','url')
        cls.service = cls.conf.get_value('service','dynamic')
        cls.ro = ReplaceOperte()
        cls.run_main = RunMain()
        cls.token = Login().login()
        GlobalDict().set_dict('token',cls.token )


    @ddt.data(*login)
    def test_run_main(self,data):

        method = data['method']
        url = self.request_url + self.service + data['path']

        header = data['header']
        if re.search(r'\${.+?}',header):
            self.ro.replace_excel(header)
        header = json.loads(header)

        params = data['params']
        if re.search(r'\${.+?}', params):
            self.ro.replace_excel(params)
        params = json.loads(params)
        global_value = data['global']

        result = self.run_main.run_main(method, url=url, data=params, header=header)
        if global_value.startswith('{'):
            global_value = eval(global_value)
        self.ro.replace_global_value(global_value,result)



if __name__ == '__main__':
    unittest.main()