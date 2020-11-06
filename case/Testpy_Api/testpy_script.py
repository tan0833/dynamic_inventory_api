'''基于pytest测试框架的接口测试'''

from common.get_excel_case_list import ChainExcelData
import pytest
from common.replace_opertate import ReplaceOperte
from common.save_api_params import SaveApiParams
from config.Log import Log
from config.get_conf import Conf
from runMain.run_main import RunMain
from config.global_dict import temp_dict
from time import sleep


chain_excel_data = ChainExcelData()

class TestApi:

    def setup_class(self):
        self.conf = Conf()
        self.log = Log()
        self.request_url = self.conf.get_value('request_url', 'url')
        self.environment_name = self.conf.is_url(self.request_url)
        self.service = self.conf.get_value('service', 'waybill_query')
        self.ro = ReplaceOperte(temp_dict)
        self.save_params = SaveApiParams(temp_dict)
        self.run_main = RunMain()


    @pytest.mark.parametrize('data',chain_excel_data.excel_case_generator())
    def test_api(self,data):
        case_name = data['case_name']
        case_id = data['case_id']
        self._testMethodDoc = case_name
        self._testMethodName = '%s测试' % self.environment_name
        self.log.info('=======执行第%s条用例开始： %s ========' % (case_id, case_name))
        method = data['method']
        url = self.request_url + self.ro.replace_excel(data['path'])

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

        sleep_value = data['sleep']
        try:
            int(sleep_value)
            sleep(int(sleep_value))
        except ValueError as e:
            pass

        result = self.run_main.run_main(method, url=url, data=params, header=header, file=file)
        self.ro.replace_global_value(global_value, result, params=params)
        self.save_params.save_params()

        expect = data['expect']
        if expect.startswith('['):
            expect = eval(expect)
            assert_res = self.ro.replace_expect_pytest(expect, result)
            for i in assert_res:
                # self.log.info('断言结果：%s'%i)
                exec(i)


if __name__ == '__main__':
    pytest.main(["-s", "testpy_script.py"])  # 调用pytest的main函数执行测试
