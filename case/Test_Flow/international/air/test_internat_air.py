'''
国际空运下单基础数据下拉列表
'''

from api_pack.api_business.basic_data_api import BasicData
from api_pack.api_business.internation_air_api import InternatAirApi
import pytest,allure,jsonpath,unittest,ddt
from util.create_random import CreateRandom
from config.Log import Log
from config.global_dict import temp_dict,temp_list


basic_data = BasicData(temp_dict)



#提单类型
lading_bill_type = basic_data.lading_bill_types(mode='TPM_AIR',transnationalShipment=True)
lading_bill_type_list = jsonpath.jsonpath(lading_bill_type,'$..id')

#贸易术语
incoterm_types = basic_data.incoterm_types(mode='TPM_AIR',transnationalShipment=True)
incoterm_type_list = jsonpath.jsonpath(incoterm_types,'$..id')


#包装单位
package_unit_types = basic_data.package_unit_types(mode='TPM_AIR',transnationalShipment=True)
package_unit_types_list = jsonpath.jsonpath(package_unit_types,'$..id')


#货物明细包装单位
line_package_unit_types = basic_data.line_package_unit_types(mode='TPM_AIR',transnationalShipment=True)
line_package_unit_types_list = jsonpath.jsonpath(line_package_unit_types,'$..id')


#货币类型
currency_type = basic_data.currency_types(mode='TPM_AIR',transnationalShipment=True)
currency_type_list = jsonpath.jsonpath(currency_type,'$..code')


#服务类型
server_level = basic_data.server_level(mode='TPM_AIR',transnationalShipment=True,loadingType='CTM_FTL')
server_level_list = jsonpath.jsonpath(server_level,'$..id')



@ddt.ddt
class TestInternatSea(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.internat_air = InternatAirApi(temp_dict)
        cls.log = Log()
        cls.mock_data = CreateRandom()


    # @unittest.skip
    @ddt.data(*lading_bill_type_list)
    def test_lading_bill_type(self, lading_bill_id):
        self._testMethodDoc = '国际空运遍历提单类型'
        id = None
        phone = self.mock_data.random_create_mobile_phone()
        try:
            result = self.internat_air.internat_air_save(**{'shippingInfo.billOfLadingTypeCode': lading_bill_id,'referenceOrders.0.referenceOrderNo':phone})
            id = jsonpath.jsonpath(result, '$..data')[0]
            self.assertEqual(result.get('success'), True)

            res = self.internat_air.internat_air_submit(id)
            self.assertEqual(res.get('success'), True)
        except Exception as e:
            raise e
        finally:
            self.log.warning('id:%s,提单类型：%s,参考单号：%s' % (id, lading_bill_id,phone))
            temp_list.append(id)
        self.log.info('\n\n')


    # @unittest.skip
    @ddt.data(*server_level_list)
    def test_server_level(self,server_level_id):
        self._testMethodDoc = '国际空运遍历服务类型'
        id = None
        phone = self.mock_data.random_create_mobile_phone()
        try:
            result = self.internat_air.internat_air_save(
                **{'shippingInfo.serviceModeCode': server_level_id, 'referenceOrders.0.referenceOrderNo': phone})
            id = jsonpath.jsonpath(result, '$..data')[0]
            self.assertEqual(result.get('success'), True)

            res = self.internat_air.internat_air_submit(id)
            self.assertEqual(res.get('success'), True)
        except Exception as e:
            raise e
        finally:
            self.log.warning('id:%s,服务类型：%s,参考单号：%s' % (id, server_level_id, phone))
            temp_list.append(id)
        self.log.info('\n\n')

    # @unittest.skip
    @ddt.data(*incoterm_type_list)
    def test_incoterm_type(self,incoterm_type_id):
        self._testMethodDoc = '国际空运遍历贸易术语'
        id = None
        phone = self.mock_data.random_create_mobile_phone()
        try:
            result = self.internat_air.internat_air_save(
                **{'shippingInfo.incotermsCode': incoterm_type_id, 'referenceOrders.0.referenceOrderNo': phone})
            id = jsonpath.jsonpath(result, '$..data')[0]
            self.assertEqual(result.get('success'), True)

            res = self.internat_air.internat_air_submit(id)
            self.assertEqual(res.get('success'), True)
        except Exception as e:
            raise e
        finally:
            self.log.warning('id:%s,贸易术语：%s，参考单号：%s' % (id, incoterm_type_id,phone))
            temp_list.append(id)
        self.log.info('\n\n')


    # @unittest.skip
    @ddt.data(*package_unit_types_list)
    def test_package_unit_types(self, package_unit_type_id):
        self._testMethodDoc = '国际空运遍历包装单位'
        id = None
        phone = self.mock_data.random_create_mobile_phone()
        try:
            result = self.internat_air.internat_air_save(
                **{'cargoInfo.totalPackageQtyUnitCode': package_unit_type_id, 'referenceOrders.0.referenceOrderNo': phone})
            id = jsonpath.jsonpath(result, '$..data')[0]
            self.assertEqual(result.get('success'), True)

            res = self.internat_air.internat_air_submit(id)
            self.assertEqual(res.get('success'), True)
        except Exception as e:
            raise e
        finally:
            self.log.warning('id:%s,包装单位：%s，参考单号：%s' % (id, package_unit_type_id, phone))
            temp_list.append(id)
        self.log.info('\n\n')

    # @unittest.skip
    @ddt.data(*line_package_unit_types_list)
    def test_line_package_unit_types(self, line_package_unit_types_id):
        self._testMethodDoc = '国际空运遍历货物明细包装单位'
        id = None
        phone = self.mock_data.random_create_mobile_phone()
        try:
            result = self.internat_air.internat_air_save(
                **{'cargoInfo.cargoInfoLines.0.packageUnitCode': line_package_unit_types_id,
                   'referenceOrders.0.referenceOrderNo': phone})
            id = jsonpath.jsonpath(result, '$..data')[0]
            self.assertEqual(result.get('success'), True)

            res = self.internat_air.internat_air_submit(id)
            self.assertEqual(res.get('success'), True)
        except Exception as e:
            raise e
        finally:
            self.log.warning('id:%s,货物明细包装单位：%s，参考单号：%s' % (id, line_package_unit_types_id, phone))
            temp_list.append(id)
        self.log.info('\n\n')

    # @unittest.skip
    @ddt.data(*currency_type_list)
    def test_currency_type_list(self, currency_type_list_id):
        self._testMethodDoc = '国际空运遍历货物明细货币和保价货币'
        id = None
        phone = self.mock_data.random_create_mobile_phone()
        try:
            result = self.internat_air.internat_air_save(
                **{'cargoInfo.cargoInfoLines.0.currencyCode': currency_type_list_id,
                   'valueAddedBusiness.currencyCode': currency_type_list_id,
                   'referenceOrders.0.referenceOrderNo': phone})
            id = jsonpath.jsonpath(result, '$..data')[0]
            self.assertEqual(result.get('success'), True)

            res = self.internat_air.internat_air_submit(id)
            self.assertEqual(res.get('success'), True)
        except Exception as e:
            raise e
        finally:
            self.log.warning('id:%s,货币：%s，参考单号：%s' % (id, currency_type_list_id, phone))
            temp_list.append(id)
        self.log.info('\n\n')



if __name__ == '__main__':
    unittest.main()