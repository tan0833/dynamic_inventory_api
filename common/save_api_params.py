'''
8种运输模式保存的数据写入ymal文件，便于快速造数据
'''
from config.get_conf import Conf


class SaveApiParams:

    def __init__(self,global_dict):
        self.global_dict = global_dict
        self.conf = Conf()
        self.basic_url = self.conf.get_value('request_url','url')
        self.environment_name = self.conf.is_url(self.basic_url)


    def save_params(self):
        '''
        组合所有运输方式
        :return:
        '''
        self.save_domestic_road_params()
        self.save_domestic_air_params()
        self.save_domestic_sea_params()
        self.save_domestic_rail_params()
        self.save_domestic_express_params()
        self.save_international_air_params()
        self.save_international_express_params()
        self.save_international_sea_params()


    def save_domestic_road_params(self):
        '''
        将国内陆运保存的参数写入json文件中
        :return:
        '''
        road_json_file = self.conf.get_file_path('api_pack','api_params',self.environment_name,'domestic_road_save_api_params.json')
        demestic_road_data = self.global_dict.get('save_demestic_road_params')
        if demestic_road_data != None:
            self.conf.write_json(demestic_road_data,road_json_file)


    def save_domestic_sea_params(self):
        '''
        将国内海运保存的参数写入json文件中
        :return:
        '''
        sea_json_file = self.conf.get_file_path('api_pack','api_params',self.environment_name,'domestic_sea_save_api_params.json')
        demestic_sea_data = self.global_dict.get('save_demestic_sea_params')
        if demestic_sea_data != None:
            self.conf.write_json(demestic_sea_data,sea_json_file)

    def save_domestic_air_params(self):
        '''
        将国内空运保存的参数写入json文件中
        :return:
        '''
        air_json_file = self.conf.get_file_path('api_pack', 'api_params', self.environment_name,
                                                'domestic_air_save_api_params.json')
        demestic_air_data = self.global_dict.get('save_demestic_air_params')
        if demestic_air_data != None:
            self.conf.write_json(demestic_air_data, air_json_file)

    def save_domestic_rail_params(self):
        '''
        将国内铁运保存的参数写入json文件中
        :return:
        '''
        rail_json_file = self.conf.get_file_path('api_pack','api_params',self.environment_name,'domestic_rail_save_api_params.json')
        demestic_rail_data = self.global_dict.get('save_demestic_rail_params')
        if demestic_rail_data != None:
            self.conf.write_json(demestic_rail_data,rail_json_file)

    def save_domestic_express_params(self):
        '''
        将国内快递保存的参数写入json文件中
        :return:
        '''
        express_json_file = self.conf.get_file_path('api_pack','api_params',self.environment_name,'domestic_express_save_api_params.json')
        demestic_express_data = self.global_dict.get('save_demestic_express_params')
        if demestic_express_data != None:
            self.conf.write_json(demestic_express_data,express_json_file)

    def save_international_express_params(self):
        '''
        将国际快递保存的参数写入json文件中
        :return:
        '''
        express_json_file = self.conf.get_file_path('api_pack', 'api_params', self.environment_name,
                                                    'international_express_save_api_params.json')
        international_express_data = self.global_dict.get('save_international_express_params')
        if international_express_data != None:
            self.conf.write_json(international_express_data, express_json_file)

    def save_international_sea_params(self):
        '''
        将国际海运保存的参数写入json文件中
        :return:
        '''
        sea_json_file = self.conf.get_file_path('api_pack', 'api_params', self.environment_name,
                                                'international_sea_save_api_params.json')
        international_sea_data = self.global_dict.get('save_international_sea_params')
        if international_sea_data != None:
            self.conf.write_json(international_sea_data, sea_json_file)

    def save_international_air_params(self):
        '''
        将国际空运保存的参数写入json文件中
        :return:
        '''
        air_json_file = self.conf.get_file_path('api_pack', 'api_params', self.environment_name,
                                                'international_air_save_api_params.json')
        international_air_data = self.global_dict.get('save_international_air_params')
        if international_air_data != None:
            self.conf.write_json(international_air_data, air_json_file)


if __name__ == '__main__':
    a = {"save_demestic_air_params":{"aa":"张三李四","bb":13}}
    s = SaveApiParams(a)
    s.save_params()
