from config.get_conf import Conf
from runMain.run_main import RunMain


class BasicData:

    def __init__(self,dict):
        self.conf = Conf()
        self.basic_url = self.conf.get_value('request_url','url')
        self.basic_dict = self.conf.get_yaml(self.conf.get_file_path('api_pack','api_config','basic_data_api_conf.yml'))
        self.runner = RunMain()
        self.token = dict.get('token')

    def server_level(self,mode='TPM_SEA',loadingType=None,transnationalShipment=True):
        '''
        服务类型
        :param mode: 运输模式
        :param transnationalShipment: 输入参数
        :param loadingType: 配载方式
        :return:
        '''
        server_level_dict = self.basic_dict.get('server_level')
        url = self.basic_url + server_level_dict.get('url')
        method = server_level_dict.get('method')
        params = server_level_dict.get('params')
        params['shippingMode']='%s'%mode
        params['loadingType'] = '%s'%loadingType
        params['transnationalShipment'] = transnationalShipment

        header = self.basic_dict.get('header')
        header['Authorization'] = '%s'%self.token
        result = self.runner.run_main(method=method,url=url,data=params,header=header)
        return result

    def international_areas(self):
        '''
        电话区号
        :return:
        '''
        international_areas_dict = self.basic_dict.get('international_areas')
        url = self.basic_url + international_areas_dict.get('url')
        method = international_areas_dict.get('method')
        header = self.basic_dict.get('header')
        header['Authorization'] = '%s' % self.token
        result = self.runner.run_main(method=method, url=url,  header=header,data=None)
        return result

    def paying_types(self,mode='TPM_SEA',transnationalShipment=True):
        '''
        付款方式
        :param mode: 运输方式code
        :param transnationalShipment: 是否国际
        :return:
        '''
        paying_types_dict = self.basic_dict.get('paying_types')
        url = self.basic_url + paying_types_dict.get('url')
        method = paying_types_dict.get('method')
        params = paying_types_dict.get('params')
        params['shippingMode'] = '%s' % mode
        params['transnationalShipment'] = transnationalShipment

        header = self.basic_dict.get('header')
        header['Authorization'] = '%s' % self.token
        result = self.runner.run_main(method=method, url=url, data=params, header=header)
        return result

    def vehicle_type(self):
        '''
        车辆类型
        :return:
        '''
        vehicle_type_dict = self.basic_dict.get('vehicle_type')
        url = self.basic_url + vehicle_type_dict.get('url')
        method = vehicle_type_dict.get('method')
        params = vehicle_type_dict.get('params')

        header = self.basic_dict.get('header')
        header['Authorization'] = '%s' % self.token
        result = self.runner.run_main(method=method, url=url, data=params, header=header)
        return result

    def vehicle_specification(self,vehicleSpeciesCodeEq):
        '''
        车辆规格
        :param vehicleSpeciesCodeEq:
        :return:
        '''
        vehicle_specification_dict = self.basic_dict.get('vehicle_specification')
        url = self.basic_url + vehicle_specification_dict.get('url')
        method = vehicle_specification_dict.get('method')
        params = vehicle_specification_dict.get('params')
        params['vehicleSpeciesCodeEq'] = '%s'%vehicleSpeciesCodeEq

        header = self.basic_dict.get('header')
        header['Authorization'] = '%s' % self.token
        result = self.runner.run_main(method=method, url=url, data=params, header=header)
        return result

    def customs_supervision(self,specificationEq,vehicleSpeciesCodeEq):
        '''
        是否海关监管
        :param specificationEq:
        :param vehicleSpeciesCodeEq:
        :return:
        '''
        customs_supervision_dict = self.basic_dict.get('customs_supervision')
        url = self.basic_url + customs_supervision_dict.get('url')
        method = customs_supervision_dict.get('method')
        params = customs_supervision_dict.get('params')
        params['specificationEq'] = '%s' % specificationEq
        params['vehicleSpeciesCodeEq'] = '%s'%vehicleSpeciesCodeEq

        header = self.basic_dict.get('header')
        header['Authorization'] = '%s' % self.token
        result = self.runner.run_main(method=method, url=url, data=params, header=header)
        return result


    def container_mode(self,mode='TPM_SEA',transnationalShipment=True):
        '''
        配载方式
        :param mode:
        :param transnationalShipment:
        :return:
        '''
        container_mode_dict = self.basic_dict.get('container_mode')
        url = self.basic_url + container_mode_dict.get('url')
        method = container_mode_dict.get('method')
        params = container_mode_dict.get('params')
        params['shippingMode'] = '%s' % mode
        params['transnationalShipment'] = transnationalShipment

        header = self.basic_dict.get('header')
        header['Authorization'] = '%s' % self.token
        result = self.runner.run_main(method=method, url=url, data=params, header=header)
        return result

    def container_types(self):
        '''
        集装箱类型
        :return:
        '''
        container_types_dict = self.basic_dict.get('container_types')
        url = self.basic_url + container_types_dict.get('url')
        method = container_types_dict.get('method')
        params = container_types_dict.get('params')

        header = self.basic_dict.get('header')
        header['Authorization'] = '%s' % self.token
        result = self.runner.run_main(method=method, url=url, data=params, header=header)
        return result

    def container_size(self,mode='TPM_SEA',transnationalShipment=True):
        '''
        集装箱尺寸
        :param transnationalShipment:
        :return:
        '''
        container_size_dict = self.basic_dict.get('container_size')
        url = self.basic_url + container_size_dict.get('url')
        method = container_size_dict.get('method')
        params = container_size_dict.get('params')
        params['shippingMode'] = '%s' % mode
        params['transnationalShipment'] = transnationalShipment

        header = self.basic_dict.get('header')
        header['Authorization'] = '%s' % self.token
        result = self.runner.run_main(method=method, url=url, data=params, header=header)
        return result

    def lading_bill_types(self,mode='TPM_SEA',transnationalShipment=True):
        '''
        提单类型
        :param mode:
        :param transnationalShipment:
        :return:
        '''
        lading_bill_types_dict = self.basic_dict.get('lading_bill_types')
        url = self.basic_url + lading_bill_types_dict.get('url')
        method = lading_bill_types_dict.get('method')
        params = lading_bill_types_dict.get('params')
        params['shippingMode'] = '%s' % mode
        params['transnationalShipment'] = transnationalShipment

        header = self.basic_dict.get('header')
        header['Authorization'] = '%s' % self.token
        result = self.runner.run_main(method=method, url=url, data=params, header=header)
        return result

    def incoterm_types(self,mode='TPM_SEA',transnationalShipment=True):
        '''
        贸易术语
        :param mode:
        :param transnationalShipment:
        :return:
        '''
        incoterm_types_dict = self.basic_dict.get('incoterm_types')
        url = self.basic_url + incoterm_types_dict.get('url')
        method = incoterm_types_dict.get('method')
        params = incoterm_types_dict.get('params')
        params['shippingMode'] = '%s' % mode
        params['transnationalShipment'] = transnationalShipment

        header = self.basic_dict.get('header')
        header['Authorization'] = '%s' % self.token
        result = self.runner.run_main(method=method, url=url, data=params, header=header)
        return result


    def reference_order_types(self,transnationalShipment=True):
        '''
        参考单类型
        :param transnationalShipment:
        :return:
        '''
        reference_order_types_dict = self.basic_dict.get('reference_order_types')
        url = self.basic_url + reference_order_types_dict.get('url')
        method = reference_order_types_dict.get('method')
        params = reference_order_types_dict.get('params')
        params['transnationalShipment'] = transnationalShipment

        header = self.basic_dict.get('header')
        header['Authorization'] = '%s' % self.token
        result = self.runner.run_main(method=method, url=url, data=params, header=header)
        return result

    def line_package_unit_types(self,mode='TPM_SEA',transnationalShipment=True):
        '''
        货物明细包装单位
        :param mode:
        :param transnationalShipment:
        :return:
        '''
        line_package_unit_types_dict = self.basic_dict.get('line_package_unit_types')
        url = self.basic_url + line_package_unit_types_dict.get('url')
        method = line_package_unit_types_dict.get('method')
        params = line_package_unit_types_dict.get('params')
        params['shippingMode'] = '%s' % mode
        params['transnationalShipment'] = transnationalShipment

        header = self.basic_dict.get('header')
        header['Authorization'] = '%s' % self.token
        result = self.runner.run_main(method=method, url=url, data=params, header=header)
        return result


    def currency_types(self,mode='TPM_SEA',transnationalShipment=True):
        '''
        货币类型
        :param mode:
        :param transnationalShipment:
        :return:
        '''
        currency_types_dict = self.basic_dict.get('currency_types')
        url = self.basic_url + currency_types_dict.get('url')
        method = currency_types_dict.get('method')
        params = currency_types_dict.get('params')
        params['shippingMode'] = '%s' % mode
        params['transnationalShipment'] = transnationalShipment

        header = self.basic_dict.get('header')
        header['Authorization'] = '%s' % self.token
        result = self.runner.run_main(method=method, url=url, data=params, header=header)
        return result


    def package_unit_types(self):
        '''
        包装单位类型
        :return:
        '''
        package_unit_types_dict = self.basic_dict.get('package_unit_types')
        url = self.basic_url + package_unit_types_dict.get('url')
        method = package_unit_types_dict.get('method')
        params = package_unit_types_dict.get('params')

        header = self.basic_dict.get('header')
        header['Authorization'] = '%s' % self.token
        result = self.runner.run_main(method=method, url=url, data=params, header=header)
        return result

    def file_types(self,mode='TPM_SEA',transnationalShipment=True):
        '''
        附件类型
        :param mode:
        :param transnationalShipment:
        :return:
        '''
        file_types_dict = self.basic_dict.get('file_types')
        url = self.basic_url + file_types_dict.get('url')
        method = file_types_dict.get('method')
        params = file_types_dict.get('params')
        params['shippingMode'] = '%s' % mode
        params['transnationalShipment'] = transnationalShipment

        header = self.basic_dict.get('header')
        header['Authorization'] = '%s' % self.token
        result = self.runner.run_main(method=method, url=url, data=params, header=header)
        return result

    def cargo_types(self):
        '''
        货物类型
        :return:
        '''
        cargo_types_dict = self.basic_dict.get('cargo_types')
        url = self.basic_url + cargo_types_dict.get('url')
        method = cargo_types_dict.get('method')
        params = cargo_types_dict.get('params')

        header = self.basic_dict.get('header')
        header['Authorization'] = '%s' % self.token
        result = self.runner.run_main(method=method, url=url, data=params, header=header)
        return result

    def transportation_types(self):
        '''
        运输方式
        :return:
        '''
        transportation_types_dict = self.basic_dict.get('transportation_types')
        url = self.basic_url + transportation_types_dict.get('url')
        method = transportation_types_dict.get('method')
        params = transportation_types_dict.get('params')

        header = self.basic_dict.get('header')
        header['Authorization'] = '%s' % self.token
        result = self.runner.run_main(method=method, url=url, data=params, header=header)
        return result

    def bonded_areas(self):
        '''
        一日游区域
        :return:
        '''
        bonded_areas_dict = self.basic_dict.get('bonded_areas')
        url = self.basic_url + bonded_areas_dict.get('url')
        method = bonded_areas_dict.get('method')
        params = bonded_areas_dict.get('params')

        header = self.basic_dict.get('header')
        header['Authorization'] = '%s' % self.token
        result = self.runner.run_main(method=method, url=url, data=params, header=header)
        return result

    def blp_file_modes(self):
        '''
        一日游文件
        :return:
        '''
        blp_file_modes_dict = self.basic_dict.get('blp_file_modes')
        url = self.basic_url + blp_file_modes_dict.get('url')
        method = blp_file_modes_dict.get('method')
        params = blp_file_modes_dict.get('params')

        header = self.basic_dict.get('header')
        header['Authorization'] = '%s' % self.token
        result = self.runner.run_main(method=method, url=url, data=params, header=header)
        return result

    def transport_station(self,nameOrNameLocalLike=None):
        '''
        车站查询
        :param nameOrNameLocalLike:
        :return:
        '''
        transport_station_dict = self.basic_dict.get('transport_station')
        url = self.basic_url + transport_station_dict.get('url')
        method = transport_station_dict.get('method')
        params = transport_station_dict.get('params')
        params['nameOrNameLocalLike'] = '%s' % nameOrNameLocalLike

        header = self.basic_dict.get('header')
        header['Authorization'] = '%s' % self.token
        result = self.runner.run_main(method=method, url=url, data=params, header=header)
        return result


    def ports_search(self,codeOrNameOrLocalLike=None,portType='PTT_AIRPORT',mode='TPM_AIR',):
        '''
        港口/机场查询
        :param codeOrNameOrLocalLike: 需要查询的港口
        :param portType: PTT_HARBOUR,PTT_AIRPORT
        :param mode: TPM_AIR,TPM_SEA
        :return:
        '''
        ports_search_dict = self.basic_dict.get('ports_search')
        url = self.basic_url + ports_search_dict.get('url')
        method = ports_search_dict.get('method')
        params = ports_search_dict.get('params')
        params['codeOrNameOrLocalLike'] = '%s'%codeOrNameOrLocalLike
        params['portType'] = '%s' % portType
        params['shippingMode'] = '%s' % mode

        header = self.basic_dict.get('header')
        header['Authorization'] = '%s' % self.token
        result = self.runner.run_main(method=method, url=url, data=params, header=header)
        return result

    def transport_location_search(self,idOrNameOrLocalLike=''):
        '''
        城市五字码查询
        :param idOrNameOrLocalLike: 输入城市名称，五字码
        :return:
        '''
        transport_location_search_dict = self.basic_dict.get('transport_location_search')
        url = self.basic_url + transport_location_search_dict.get('url')
        method = transport_location_search_dict.get('method')
        params = transport_location_search_dict.get('params')
        params['transportLocationSearchCondition']['idOrNameOrLocalLike'] = '%s'%idOrNameOrLocalLike

        header = self.basic_dict.get('header')
        header['Authorization'] = '%s' % self.token
        result = self.runner.run_main(method=method, url=url, data=params, header=header)
        return result

if __name__ == '__main__':
    from config.global_dict import temp_dict
    b = BasicData(temp_dict)
    # a = b.server_level(loadingType='CTM_LCL')
    a = b.transport_location_search()
    # a= b.ports_search(codeOrNameOrLocalLike='',mode='TMP_SEA',portType='PTT_HARBOUR')
    # a = b.transport_station(nameOrNameLocalLike='武汉')
    # a = b.vehicle_specification('TKG_SPC')
    # a = b.customs_supervision(specificationEq='TKT_20FR',vehicleSpeciesCodeEq='TKG_SPC')

    print(type(a))
