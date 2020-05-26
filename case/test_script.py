import unittest,ddt
from common.replace_opertate import ReplaceOperte
from config.Log import Log
from config.get_conf import Conf
from util.operate_excel import Operate_excel
from runMain.run_main import RunMain
from util.operate_global import GlobalDict

#定义全局字典
temp_dict = {}
#环境地址
environment_url = Conf().get_value('request_url','url')
#环境名称
environment_name = Conf().is_url(environment_url)

res = Operate_excel(Conf().get_file_path('data','运输下单测试用例-%s.xlsx'%environment_name),"登录")
login = res.excel_dict()

r = Operate_excel(Conf().get_file_path('data','运输下单测试用例-%s.xlsx'%environment_name),"基础数据")
d = r.excel_dict()

r = Operate_excel(Conf().get_file_path('data','运输下单测试用例-%s.xlsx'%environment_name),"国内陆运")
d1 = r.excel_dict()

r = Operate_excel(Conf().get_file_path('data','运输下单测试用例-%s.xlsx'%environment_name),"运输需求")
d2 = r.excel_dict()
d1.extend(d2)



@ddt.ddt
class TestRunMain(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.conf = Conf()
        cls.log = Log()
        cls.request_url = cls.conf.get_value('request_url','url')
        cls.service = cls.conf.get_value('service','waybill_query')
        cls.ro = ReplaceOperte(temp_dict)
        cls.run_main = RunMain()


    @ddt.data(*login)
    def test_a_login(self,data):
        '''
        测试登录
        :param data:
        :return:
        '''
        case_name = data['case_name']
        case_id = data['case_id']
        self._testMethodDoc = case_name
        self.log.info('=======执行第%s条用例开始： %s ========'%(case_id,case_name))
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

        file = data['file']
        file = self.ro.replace_excel(file)
        if file.startswith('[') or file.startswith('{'):
            file = eval(file)

        global_value = data['global']
        if global_value.startswith('{'):
            global_value = eval(global_value)

        result = self.run_main.run_main(method, url=url, data=params, header=header,file=file)
        self.ro.replace_global_value(global_value,result)

        expect = data['expect']
        if expect.startswith('['):
            expect = eval(expect)
            assert_res = self.ro.replace_expect(expect, result)
            for i in assert_res:
                self.log.info('断言结果：%s' % i)
                eval(i)
        self.log.info('\n\n' )

    # @unittest.skip
    @ddt.data(*d)
    def test_b_run_main(self,data):
        case_name = data['case_name']
        case_id = data['case_id']
        self._testMethodDoc = case_name
        self.log.info('=======执行第%s条用例开始： %s ========' % (case_id, case_name))
        method = data['method']
        # url = self.request_url + self.service + self.ro.replace_excel(data['path'])
        url = self.request_url +  self.ro.replace_excel(data['path'])

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

        file = data['file']
        file = self.ro.replace_excel(file)
        if file.startswith('[') or file.startswith('{'):
            file = eval(file)

        result = self.run_main.run_main(method, url=url, data=params, header=header,file=file)
        self.ro.replace_global_value(global_value, result)

        expect = data['expect']
        if expect.startswith('['):
            expect = eval(expect)
            assert_res = self.ro.replace_expect(expect,result)
            for i in assert_res:
                self.log.info('断言结果：%s'%i)
                eval(i)
        self.log.info('\n\n')

    @ddt.data(*d1)
    def test_c_run_main(self, data):
        case_name = data['case_name']
        case_id = data['case_id']
        self._testMethodDoc = case_name
        self.log.info('=======执行第%s条用例开始： %s ========' % (case_id, case_name))
        method = data['method']
        # url = self.request_url + self.service + self.ro.replace_excel(data['path'])
        url = self.request_url + self.ro.replace_excel(data['path'])

        header = data['header']
        header = self.ro.replace_excel(header)
        if header.startswith('{'):
            header = eval(header)

        params = data['params']
        params = self.ro.replace_excel(params)
        if params.startswith('{'):
            params = eval(params)

        file = data['file']
        file = self.ro.replace_excel(file)
        if file.startswith('[') or file.startswith('{'):
            file = eval(file)

        global_value = data['global']
        if global_value.startswith('{'):
            global_value = eval(global_value)

        result = self.run_main.run_main(method, url=url, data=params, header=header,file=file)
        self.ro.replace_global_value(global_value, result)

        expect = data['expect']
        if expect.startswith('['):
            expect = eval(expect)
            assert_res = self.ro.replace_expect(expect, result)
            for i in assert_res:
                self.log.info('断言结果：%s' % i)
                eval(i)
        self.log.info('\n\n')


if __name__ == '__main__':
    unittest.main()