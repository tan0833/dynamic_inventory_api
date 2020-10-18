'''
国际海运下单基础数据下拉列表
'''

from api_pack.api_business.basic_data_api import BasicData
from api_pack.api_business.internation_sea_api import InternatSeaApi
import pytest,allure,jsonpath,unittest,ddt
from util.create_random import CreateRandom
from config.Log import Log
from config.global_dict import temp_dict,temp_list


basic_data = BasicData(temp_dict)



#提单类型
lading_bill_type = basic_data.lading_bill_types(mode='TPM_SEA',transnationalShipment=True)
lading_bill_type_list = jsonpath.jsonpath(lading_bill_type,'$..id')

#贸易术语
incoterm_types = basic_data.incoterm_types(mode='TPM_SEA',transnationalShipment=True)
incoterm_type_list = jsonpath.jsonpath(incoterm_types,'$..id')


#包装单位
package_unit_types = basic_data.package_unit_types(mode='TPM_SEA',transnationalShipment=True)
package_unit_types_list = jsonpath.jsonpath(package_unit_types,'$..id')


#货物明细包装单位
line_package_unit_types = basic_data.line_package_unit_types(mode='TPM_SEA',transnationalShipment=True)
line_package_unit_types_list = jsonpath.jsonpath(line_package_unit_types,'$..id')


#货币类型
currency_type = basic_data.currency_types(mode='TPM_SEA',transnationalShipment=True)
currency_type_list = jsonpath.jsonpath(currency_type,'$..code')

#服务类型
def server_level():
    # 配载方式
    container_server_level_list = []
    container_mode = basic_data.container_mode(mode='TPM_SEA', transnationalShipment=True)
    container_mode_list = jsonpath.jsonpath(container_mode, '$..id')
    for container_type in container_mode_list:
        server_level = basic_data.server_level(mode='TPM_SEA', loadingType=container_type, transnationalShipment=True)
        server_level_list = jsonpath.jsonpath(server_level, '$..id')
        for i in server_level_list:
            phone = CreateRandom().random_create_mobile_phone()
            temp_server_dict = {}
            temp_server_dict["container_type"] = container_type
            temp_server_dict["server_type"] = i
            temp_server_dict["phone"] = phone
            container_server_level_list.append(temp_server_dict)
    return container_server_level_list


@ddt.ddt
class TestInternatSea(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.internat_sea = InternatSeaApi(temp_dict)
        cls.log = Log()
        cls.mock_data = CreateRandom()


    @unittest.skip
    @ddt.data(*lading_bill_type_list)
    def test_lading_bill_type(self, lading_bill_id):
        self._testMethodDoc = '国际海运遍历提单类型'
        id = None
        phone = self.mock_data.random_create_mobile_phone()
        try:
            result = self.internat_sea.internat_sea_save(**{'shippingInfo.billOfLadingTypeCode': lading_bill_id,'referenceOrders.0.referenceOrderNo':phone})
            id = jsonpath.jsonpath(result, '$..data')[0]
            self.assertEqual(result.get('success'), True)

            res = self.internat_sea.internat_sea_submit(id)
            self.assertEqual(res.get('success'), True)
        except Exception as e:
            raise e
        finally:
            self.log.warning('国际海运id:%s,提单类型：%s,参考单号：%s' % (id, lading_bill_id,phone))
            temp_list.append(id)
        self.log.info('\n\n')


    # @unittest.skip
    @ddt.data(*server_level())
    def test_container_or_server_level(self,server_type):
        self._testMethodDoc = '国际海运遍历配载方式和服务类型'
        id = None
        try:
            result = self.internat_sea.internat_sea_save(**{'shippingInfo.loadingTypeCode': server_type["container_type"],
                                                            'shippingInfo.serviceModeCode': server_type["server_type"],
                                                            'referenceOrders.0.referenceOrderNo':server_type["phone"]})
            id = jsonpath.jsonpath(result, '$..data')[0]
            self.assertEqual(result.get('success'), True)

            res = self.internat_sea.internat_sea_submit(id)
            self.assertEqual(res.get('success'), True)
        except Exception as e:
            raise e
        finally:
            self.log.warning('国际海运id:%s,配载方式：%s,服务类型：%s,参考单号：%s' % (id, server_type["container_type"],server_type["server_type"],server_type["phone"]))
            temp_list.append(id)
        self.log.info('\n\n')


    @unittest.skip
    @ddt.data(*incoterm_type_list)
    def test_incoterm_type(self,incoterm_type_id):
        self._testMethodDoc = '国际海运遍历贸易术语'
        id = None
        phone = self.mock_data.random_create_mobile_phone()
        try:
            result = self.internat_sea.internat_sea_save(
                **{'shippingInfo.incotermsCode': incoterm_type_id, 'referenceOrders.0.referenceOrderNo': phone})
            id = jsonpath.jsonpath(result, '$..data')[0]
            self.assertEqual(result.get('success'), True)

            res = self.internat_sea.internat_sea_submit(id)
            self.assertEqual(res.get('success'), True)
        except Exception as e:
            raise e
        finally:
            self.log.warning('国际海运id:%s,贸易术语：%s，参考单号：%s' % (id, incoterm_type_id,phone))
            temp_list.append(id)
        self.log.info('\n\n')

    @unittest.skip
    def test_container_type_or_size(self):
        self._testMethodDoc = '国际海运遍历集装箱类型和尺寸'
        id = None

        # 集装箱类型
        container_type = basic_data.container_types()
        container_type_list = jsonpath.jsonpath(container_type, '$..id')
        for container_type in container_type_list:
            container_size = basic_data.container_size(mode='TPM_SEA',transnationalShipment=True)
            container_size_list = jsonpath.jsonpath(container_size,'$..id')
            for i in container_size_list:
                phone = self.mock_data.random_create_mobile_phone()
                try:
                    result = self.internat_sea.internat_sea_save(**{'shippingInfo.loadingTypeCode': 'CTM_FCL',
                                                                    'shippingInfo.containerInfos.0.containerTypeCode': container_type,
                                                                    'shippingInfo.containerInfos.0.containerSizeCode': i,
                                                                    'referenceOrders.0.referenceOrderNo':phone})
                    id = jsonpath.jsonpath(result, '$..data')[0]
                    self.assertEqual(result.get('success'), True)

                    res = self.internat_sea.internat_sea_submit(id)
                    self.assertEqual(res.get('success'), True)
                except Exception as e:
                    raise e
                finally:
                    self.log.warning('国际海运id:%s,集装类型：%s,集装箱尺寸：%s,参考单号：%s' % (id, container_type,i,phone))
                    temp_list.append(id)
                self.log.info('\n\n')


    @unittest.skip
    @ddt.data(*package_unit_types_list)
    def test_package_unit_types(self, package_unit_type_id):
        self._testMethodDoc = '国际海运遍历包装单位'
        id = None
        phone = self.mock_data.random_create_mobile_phone()
        try:
            result = self.internat_sea.internat_sea_save(
                **{'cargoInfo.totalPackageQtyUnitCode': package_unit_type_id, 'referenceOrders.0.referenceOrderNo': phone})
            id = jsonpath.jsonpath(result, '$..data')[0]
            self.assertEqual(result.get('success'), True)

            res = self.internat_sea.internat_sea_submit(id)
            self.assertEqual(res.get('success'), True)
        except Exception as e:
            raise e
        finally:
            self.log.warning('国际海运id:%s,包装单位：%s，参考单号：%s' % (id, package_unit_type_id, phone))
            temp_list.append(id)
        self.log.info('\n\n')

    @unittest.skip
    @ddt.data(*line_package_unit_types_list)
    def test_line_package_unit_types(self, line_package_unit_types_id):
        self._testMethodDoc = '国际海运遍历货物明细包装单位'
        id = None
        phone = self.mock_data.random_create_mobile_phone()
        try:
            result = self.internat_sea.internat_sea_save(
                **{'cargoInfo.cargoInfoLines.0.packageUnitCode': line_package_unit_types_id,
                   'referenceOrders.0.referenceOrderNo': phone})
            id = jsonpath.jsonpath(result, '$..data')[0]
            self.assertEqual(result.get('success'), True)

            res = self.internat_sea.internat_sea_submit(id)
            self.assertEqual(res.get('success'), True)
        except Exception as e:
            raise e
        finally:
            self.log.warning('国际海运id:%s,货物明细包装单位：%s，参考单号：%s' % (id, line_package_unit_types_id, phone))
            temp_list.append(id)
        self.log.info('\n\n')

    @unittest.skip
    @ddt.data(*currency_type_list)
    def test_currency_type_list(self, currency_type_list_id):
        self._testMethodDoc = '国际海运遍历货物明细货币和保价货币'
        id = None
        phone = self.mock_data.random_create_mobile_phone()
        try:
            result = self.internat_sea.internat_sea_save(
                **{'cargoInfo.cargoInfoLines.0.currencyCode': currency_type_list_id,
                   'valueAddedBusiness.currencyCode': currency_type_list_id,
                   'referenceOrders.0.referenceOrderNo': phone})
            id = jsonpath.jsonpath(result, '$..data')[0]
            self.assertEqual(result.get('success'), True)

            res = self.internat_sea.internat_sea_submit(id)
            self.assertEqual(res.get('success'), True)
        except Exception as e:
            raise e
        finally:
            self.log.warning('国际海运id:%s,货币：%s，参考单号：%s' % (id, currency_type_list_id, phone))
            temp_list.append(id)
        self.log.info('\n\n')



if __name__ == '__main__':
    unittest.main()