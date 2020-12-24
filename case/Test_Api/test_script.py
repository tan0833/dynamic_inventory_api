'''基于unittest测试框架接口测试'''

import unittest,ddt
from common.replace_opertate import ReplaceOperte
from common.save_api_params import SaveApiParams
from config.Log import Log
from config.get_conf import Conf
from util.operate_excel import Operate_excel
from runMain.run_main import RunMain
from config.global_dict import temp_dict
from time import sleep
from common.get_excel_case_list import ChainExcelData
from common.delete_test_data import DeleteTestData

chain_excel_data = ChainExcelData()


@ddt.ddt
class TestRunMain(unittest.TestCase):
    '''
    接口测试类
    '''

    @classmethod
    def setUp(cls):
        cls.conf = Conf()
        cls.log = Log()
        cls.request_url = cls.conf.get_value('request_url','url')
        cls.environment_name = cls.conf.is_url(cls.request_url)
        cls.service = cls.conf.get_value('service','waybill_query')
        cls.ro = ReplaceOperte(temp_dict)
        cls.save_params = SaveApiParams(temp_dict)
        cls.run_main = RunMain()
        cls.delete_test_data = DeleteTestData(temp_dict)


    # @unittest.skip
    @ddt.data(*chain_excel_data.excel_case_generator())
    def test_b_run_main(self,data):
        case_name = data['case_name']
        case_id = data['case_id']
        self._testMethodDoc = case_name
        self._testMethodName = '%s测试'%self.environment_name
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
        if params.startswith('{') or params.startswith('['):
            params = eval(params)

        global_value = data['global']
        if global_value.startswith('{'):
            global_value = eval(global_value)

        file = data['file']
        file = self.ro.replace_excel(file)
        if file.startswith('[') or file.startswith('{'):
            file = eval(file)


        sleep_value = data['sleep']
        try:
            int(sleep_value)
            sleep(int(sleep_value))
        except ValueError as e:
            pass

        result = self.run_main.run_main(method, url=url, data=params, header=header,file=file)
        self.ro.replace_global_value(global_value, result,params=params)
        self.save_params.save_params()
        expect = data['expect']

        if expect.startswith('['):
            expect = eval(expect)
            assert_res = self.ro.replace_expect(expect,result)
            for i in assert_res:
                # self.log.info('断言结果：%s'%i)
                exec(i)

    # def test_zdelete_order_id(self):
    #     '''
    #     删除已创建的id
    #     :return:
    #     '''
    #
    #     self._testMethodDoc = '清除已创建的订单id'
    #     self._testMethodName = '清除脚本创建测试数据'
    #     try:
    #         self.delete_test_data.sql_delete_data()
    #     except Exception as e:
    #         raise e


    # temp_dict = temp_dict
    #
    # def test_temp_dict(self):
    #     '''
    #     查看全局字典
    #     :return:
    #     '''
    #     import json
    #     a = json.dumps(temp_dict, sort_keys=True, indent=4, separators=(',', ':'),
    #                                              ensure_ascii=False)
    #     self.log.info(a)




if __name__ == '__main__':
    unittest.main()

