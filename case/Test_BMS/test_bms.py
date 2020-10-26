'''
测试对账单下载遍历
'''

from api_pack.api_bms.bms_query_download_api import BmsQueryDownloadApi
import unittest,jsonpath,ddt,time
from config.Log import Log
from config.global_dict import temp_dict,temp_list


bms = BmsQueryDownloadApi(temp_dict)
bill_no_query = bms.bms_query(**{"month":12})
bill_no_list = jsonpath.jsonpath(bill_no_query,'$..billNo')


@ddt.ddt
class TestDownloadApi(unittest.TestCase):

    @ddt.data(*bill_no_list)
    def test_download(self,bill_no):
        self._testMethodDoc = '对账单号为：%s的账单下载'%bill_no
        bms_download_res = bms.bms_download(**{"billNo":bill_no})
        self.assertIn('.xls',bms_download_res.get('Content-Disposition'))
        time.sleep(5)
        Log().info('\n\n')


if __name__ == '__main__':
    unittest.main()

