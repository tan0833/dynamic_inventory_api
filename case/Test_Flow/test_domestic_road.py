'''
国内陆运下单基础数据下拉列表
'''

from api_pack.api_business.basic_data_api import BasicData
from api_pack.api_business.domestic_road_api import DomesticRoadApi
import pytest,allure,jsonpath,unittest,ddt
from util.create_random import CreateRandom
from config.Log import Log
from config.global_dict import temp_dict


basic_data = BasicData(temp_dict)


#配载方式
loading_type = basic_data.container_mode(mode='TPM_ROAD', transnationalShipment=False)
loading_type_list = jsonpath.jsonpath(loading_type,'$..id')


#包装单位
package_unit_types = basic_data.package_unit_types()
package_unit_types_list = jsonpath.jsonpath(package_unit_types,'$..id')


#货物明细包装单位
line_package_unit_types = basic_data.line_package_unit_types(mode='TPM_ROAD', transnationalShipment=False)
line_package_unit_types_list = jsonpath.jsonpath(line_package_unit_types,'$..id')


#货币类型
currency_type = basic_data.currency_types(mode='TPM_ROAD', transnationalShipment=False)
currency_type_list = jsonpath.jsonpath(currency_type,'$..code')


#服务类型
server_level = basic_data.server_level(mode='TPM_ROAD', transnationalShipment=False,loadingType='CTM_FTL')
server_level_list = jsonpath.jsonpath(server_level,'$..id')


#一日游区域
bonded_areas = basic_data.bonded_areas()
bonded_areas_list = jsonpath.jsonpath(bonded_areas,'$..id')

#一日游文件
blp_file_modes = basic_data.blp_file_modes()
blp_file_modes_list = jsonpath.jsonpath(blp_file_modes,'$..id')


#货物类型
cargo_type = basic_data.cargo_types()
cargo_type_list = jsonpath.jsonpath(cargo_type,'$..id')

@ddt.ddt
class TestInternatSea(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.domestic_road = DomesticRoadApi(temp_dict)
        cls.log = Log()
        cls.mock_data = CreateRandom()

    @unittest.skip
    @ddt.data(*loading_type_list)
    def test_loading_type(self,loading_type_id):
        self._testMethodDoc = '国内陆运遍历配载方式'
        id = None
        phone = self.mock_data.random_create_mobile_phone()
        try:
            result = self.domestic_road.domestic_road_save(**{'shippingInfo.loadingTypeCode': loading_type_id,
                                                            'referenceOrders.0.referenceOrderNo':phone})
            id = jsonpath.jsonpath(result, '$..data')[0]
            self.assertEqual(result.get('success'),True)

            res = self.domestic_road.domestic_road_submit(id)
            self.assertEqual(res.get('success'), True)
        except Exception as e:
            raise e
        finally:
            self.log.warning('id:%s,配载方式单位为：%s,参考单号：%s' % (id, loading_type_id,phone))
        self.log.info('\n\n')


    @unittest.skip
    @ddt.data(*server_level_list)
    def test_server_level(self,server_level_id):
        self._testMethodDoc = '国内陆运遍历服务类型'
        id = None
        phone = self.mock_data.random_create_mobile_phone()
        try:
            result = self.domestic_road.domestic_road_save(
                **{'shippingInfo.serviceModeCode': server_level_id, 'referenceOrders.0.referenceOrderNo': phone})
            id = jsonpath.jsonpath(result, '$..data')[0]
            self.assertEqual(result.get('success'), True)

            res = self.domestic_road.domestic_road_submit(id)
            self.assertEqual(res.get('success'), True)
        except Exception as e:
            raise e
        finally:
            self.log.warning('id:%s,服务类型：%s,参考单号：%s' % (id, server_level_id, phone))
        self.log.info('\n\n')

    @unittest.skip
    def test_vehicle_type_or_specification_supervision(self):
        self._testMethodDoc = '国内陆运遍历车辆类型，车辆规格，是否海关监管'
        id = None
        vehicle_types = basic_data.vehicle_type()
        vehicle_type_list = jsonpath.jsonpath(vehicle_types,'$..id')
        for vehicle_type in vehicle_type_list:
            vehicle_specification = basic_data.vehicle_specification(vehicle_type)
            vehicle_specification_list = jsonpath.jsonpath(vehicle_specification,'$..id')
            for i in vehicle_specification_list:

                phone = self.mock_data.random_create_mobile_phone()
                try:
                    result = self.domestic_road.domestic_road_save(
                        **{'shippingInfo.loadingTypeCode': 'CTM_FTL',
                           'shippingInfo.vehicleInfos.0.vehicleTypeCode': vehicle_type,
                           'shippingInfo.vehicleInfos.0.vehicleSpecificationCode': i,
                           'referenceOrders.0.referenceOrderNo': phone})
                    id = jsonpath.jsonpath(result, '$..data')[0]
                    self.assertEqual(result.get('success'), True)

                    res = self.domestic_road.domestic_road_submit(id)
                    self.assertEqual(res.get('success'), True)
                except Exception as e:
                    raise e
                finally:
                    self.log.warning('id:%s,车辆类型：%s,车辆规格：%s,参考单号：%s' % (id, vehicle_type,i, phone))
                self.log.info('\n\n')

    @unittest.skip
    def test_container_type_or_size(self):
        self._testMethodDoc = '国内陆运遍历集装箱类型和尺寸'
        id = None

        # 集装箱类型
        container_type = basic_data.container_types()
        container_type_list = jsonpath.jsonpath(container_type, '$..id')
        for container_type in container_type_list:
            container_size = basic_data.container_size(mode='TPM_ROAD', transnationalShipment=False)
            container_size_list = jsonpath.jsonpath(container_size, '$..id')
            for i in container_size_list:
                phone = self.mock_data.random_create_mobile_phone()
                try:
                    result = self.domestic_road.domestic_road_save(**{'shippingInfo.loadingTypeCode': 'CTM_FCL',
                                                                    'shippingInfo.containerInfos.0.containerTypeCode': container_type,
                                                                    'shippingInfo.containerInfos.0.containerSizeCode': i,
                                                                    'referenceOrders.0.referenceOrderNo': phone})
                    id = jsonpath.jsonpath(result, '$..data')[0]
                    self.assertEqual(result.get('success'), True)

                    res = self.domestic_road.domestic_road_submit(id)
                    self.assertEqual(res.get('success'), True)
                except Exception as e:
                    raise e
                finally:
                    self.log.warning('id:%s,集装类型：%s,集装箱尺寸：%s,参考单号：%s' % (id, container_type, i, phone))
                self.log.info('\n\n')

    @unittest.skip
    @ddt.data(*bonded_areas_list)
    def test_bonded_areas(self,bonded_areas_id):
        self._testMethodDoc = '国内陆运遍历一日游区域'
        id = None
        phone = self.mock_data.random_create_mobile_phone()
        try:
            result = self.domestic_road.domestic_road_save(
                **{'shippingInfo.uturnAreaCode': bonded_areas_id, 'referenceOrders.0.referenceOrderNo': phone})
            id = jsonpath.jsonpath(result, '$..data')[0]
            self.assertEqual(result.get('success'), True)

            res = self.domestic_road.domestic_road_submit(id)
            self.assertEqual(res.get('success'), True)
        except Exception as e:
            raise e
        finally:
            self.log.warning('id:%s,一日游区域：%s,参考单号：%s' % (id, bonded_areas_id, phone))
        self.log.info('\n\n')

    @unittest.skip
    @ddt.data(*blp_file_modes_list)
    def test_blp_file_modes(self, blp_file_modes_id):
        self._testMethodDoc = '国内陆运遍历一日游文件'
        id = None
        phone = self.mock_data.random_create_mobile_phone()
        try:
            result = self.domestic_road.domestic_road_save(
                **{'shippingInfo.uturnDocumentCode': blp_file_modes_id, 'referenceOrders.0.referenceOrderNo': phone})
            id = jsonpath.jsonpath(result, '$..data')[0]
            self.assertEqual(result.get('success'), True)

            res = self.domestic_road.domestic_road_submit(id)
            self.assertEqual(res.get('success'), True)
        except Exception as e:
            raise e
        finally:
            self.log.warning('id:%s,一日游文件：%s,参考单号：%s' % (id, blp_file_modes_id, phone))
        self.log.info('\n\n')

    @unittest.skip
    @ddt.data(*cargo_type_list)
    def test_cargo_type(self, cargo_type_id):
        self._testMethodDoc = '国内陆运遍历货物类型'
        id = None
        phone = self.mock_data.random_create_mobile_phone()
        try:
            result = self.domestic_road.domestic_road_save(
                **{'cargoInfo.cargoTypeCode': cargo_type_id, 'referenceOrders.0.referenceOrderNo': phone})
            id = jsonpath.jsonpath(result, '$..data')[0]
            self.assertEqual(result.get('success'), True)

            res = self.domestic_road.domestic_road_submit(id)
            self.assertEqual(res.get('success'), True)
        except Exception as e:
            raise e
        finally:
            self.log.warning('id:%s,货物类型：%s,参考单号：%s' % (id, cargo_type_id, phone))
        self.log.info('\n\n')

    @unittest.skip
    @ddt.data(*package_unit_types_list)
    def test_package_unit_types(self, package_unit_type_id):
        self._testMethodDoc = '国内陆运遍历包装单位'
        id = None
        phone = self.mock_data.random_create_mobile_phone()
        try:
            result = self.domestic_road.domestic_road_save(
                **{'cargoInfo.totalPackageQtyUnitCode': package_unit_type_id, 'referenceOrders.0.referenceOrderNo': phone})
            id = jsonpath.jsonpath(result, '$..data')[0]
            self.assertEqual(result.get('success'), True)

            res = self.domestic_road.domestic_road_submit(id)
            self.assertEqual(res.get('success'), True)
        except Exception as e:
            raise e
        finally:
            self.log.warning('id:%s,包装单位：%s，参考单号：%s' % (id, package_unit_type_id, phone))
        self.log.info('\n\n')

    @unittest.skip
    @ddt.data(*line_package_unit_types_list)
    def test_line_package_unit_types(self, line_package_unit_types_id):
        self._testMethodDoc = '国内陆运遍历货物明细包装单位'
        id = None
        phone = self.mock_data.random_create_mobile_phone()
        try:
            result = self.domestic_road.domestic_road_save(
                **{'cargoInfo.cargoInfoLines.0.packageUnitCode': line_package_unit_types_id,
                   'referenceOrders.0.referenceOrderNo': phone})
            id = jsonpath.jsonpath(result, '$..data')[0]
            self.assertEqual(result.get('success'), True)

            res = self.domestic_road.domestic_road_submit(id)
            self.assertEqual(res.get('success'), True)
        except Exception as e:
            raise e
        finally:
            self.log.warning('id:%s,货物明细包装单位：%s，参考单号：%s' % (id, line_package_unit_types_id, phone))
        self.log.info('\n\n')

    @unittest.skip
    @ddt.data(*currency_type_list)
    def test_currency_type_list(self, currency_type_list_id):
        self._testMethodDoc = '国内陆运遍历货物明细货币和保价货币'
        id = None
        phone = self.mock_data.random_create_mobile_phone()
        try:
            result = self.domestic_road.domestic_road_save(
                **{'cargoInfo.cargoInfoLines.0.currencyCode': currency_type_list_id,
                   'valueAddedBusiness.currencyCode': currency_type_list_id,
                   'referenceOrders.0.referenceOrderNo': phone})
            id = jsonpath.jsonpath(result, '$..data')[0]
            self.assertEqual(result.get('success'), True)

            res = self.domestic_road.domestic_road_submit(id)
            self.assertEqual(res.get('success'), True)
        except Exception as e:
            raise e
        finally:
            self.log.warning('id:%s,货币：%s，参考单号：%s' % (id, currency_type_list_id, phone))
        self.log.info('\n\n')



if __name__ == '__main__':
    unittest.main()