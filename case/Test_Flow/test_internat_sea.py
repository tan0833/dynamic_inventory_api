'''
国际海运流程测试
'''

from api_pack.api_business.basic_data_api import BasicData
from api_pack.api_business.internation_sea_api import InternatSeaApi
import pytest,allure,jsonpath,unittest,ddt

from config.Log import Log
from config.global_dict import temp_dict


basic_data = BasicData(temp_dict)


def paying_types():
    '''
    付款方式
    '''
    paying_params = basic_data.paying_types(mode='TPM_SEA', transnationalShipment=True)
    paying_id_list = jsonpath.jsonpath(paying_params, '$..id')
    return paying_id_list

#提单类型
lading_bill_type = basic_data.lading_bill_types(mode='TPM_SEA',transnationalShipment=True)
lading_bill_type_list = jsonpath.jsonpath(lading_bill_type,'$..id')

#贸易术语
incoterm_types = basic_data.incoterm_types(mode='TPM_SEA',transnationalShipment=True)
incoterm_type_list = jsonpath.jsonpath(incoterm_types,'$..id')

@ddt.ddt
class TestInternatSea(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.internat_sea = InternatSeaApi(temp_dict)
        cls.log = Log()


    @ddt.data(*paying_types())
    def test_paying_types(self,paying_id):
        self._testMethodDoc = '国际海运遍历付款方式'
        id = None
        try:
            result = self.internat_sea.internat_sea_save(**{'shippingInfo.paymentTypeCode': paying_id})
            id = jsonpath.jsonpath(result, '$..data')[0]
            self.assertEqual(result.get('success'),True)

            res = self.internat_sea.internat_sea_submit(id)
            self.assertEqual(res.get('success'), True)
        except Exception as e:
            raise e
        finally:
            self.log.warning('id:%s,付款方式单位为：%s' % (id, paying_id))
        self.log.info('\n\n')

    @ddt.data(*lading_bill_type_list)
    def test_lading_bill_type(self, lading_bill_id):
        self._testMethodDoc = '国际海运遍历提单类型'
        id = None
        try:
            result = self.internat_sea.internat_sea_save(**{'shippingInfo.billOfLadingTypeCode': lading_bill_id})
            id = jsonpath.jsonpath(result, '$..data')[0]
            self.assertEqual(result.get('success'), True)

            res = self.internat_sea.internat_sea_submit(id)
            self.assertEqual(res.get('success'), True)
        except Exception as e:
            raise e
        finally:
            self.log.warning('id:%s,提单类型：%s' % (id, lading_bill_id))
        self.log.info('\n\n')

    @ddt.data(*lading_bill_type_list)
    def test_incoterm_type(self, incoterm_type_id):
        self._testMethodDoc = '国际海运遍历贸易术语'
        id = None
        try:
            result = self.internat_sea.internat_sea_save(**{'shippingInfo.incotermsCode': incoterm_type_id})
            id = jsonpath.jsonpath(result, '$..data')[0]
            self.assertEqual(result.get('success'), True)

            res = self.internat_sea.internat_sea_submit(id)
            self.assertEqual(res.get('success'), True)
        except Exception as e:
            raise e
        finally:
            self.log.warning('id:%s,贸易术语：%s' % (id, incoterm_type_id))
        self.log.info('\n\n')



if __name__ == '__main__':
    unittest.main()