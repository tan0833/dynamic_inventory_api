'''
国内海运相关接口封装
'''

from config.get_conf import Conf
from runMain.run_main import RunMain


class DomesticSeaApi:

    def __init__(self,dict):
        self.conf = Conf()
        self.basic_url = self.conf.get_value('request_url','url')
        environment_name = self.conf.is_url(self.basic_url)
        self.params = self.conf.road_json(self.conf.get_file_path('api_pack', 'api_params', environment_name,
                                                                  'domestic_sea_save_api_params.json'))
        self.basic_dict = self.conf.get_yaml(
            self.conf.get_file_path('api_pack', 'api_config', 'domestic_sea_api_conf.yml'))
        self.runner = RunMain()
        self.token = dict.get('token')


    def domestic_sea_save(self,**kwargs):
        '''
        国内海运保存，输入的kwargs字典暂时只支持一个键
        :param **kwargs: 多级字典命名方式如：{"shippingInfo.consignee.addressCode":"测试"}
        :return:
        '''
        domestic_sea_save_dict = self.basic_dict.get('domestic_sea_save')
        url = self.basic_url + domestic_sea_save_dict.get('url')
        method = domestic_sea_save_dict.get('method')
        params = self.params

        for i,j in kwargs.items():  #获取跟进字典的键
            temp_str = ''
            num = 0
            key_list = i.split('.')
            for m in key_list:
                if num == 0:
                    try:
                        m = int(m)
                        temp_str = 'params[%d]' % m
                    except Exception as e:
                        temp_str = 'params["%s"]' % m  # 判断是否是字符串，如果是字符串要加引号

                    num = num + 1
                else:
                    try:
                        m = int(m)
                        temp_str = temp_str + '[%d]' % m
                    except Exception as e:
                        temp_str = temp_str + '["%s"]' % m

            if isinstance(j,str):
                temp_str = temp_str + '="%s"'%j
            elif isinstance(j,int):
                temp_str = temp_str + '=%s' % j

            if temp_str != None:
                exec(temp_str)  #更改params的值

        header = self.basic_dict.get('header')
        header['Authorization'] = '%s'%self.token
        result = self.runner.run_main(method=method,url=url,data=params,header=header)
        return result

    def domestic_sea_submit(self,id):
        '''
        提交下单
        :param id:
        :return:
        '''
        domestic_sea_submit_dict = self.basic_dict.get('domestic_sea_submit')
        path_url = domestic_sea_submit_dict.get('url') + '%s'%id
        url = self.basic_url + path_url
        method = domestic_sea_submit_dict.get('method')
        header = self.basic_dict.get('header')

        header['Authorization'] = '%s' % self.token
        result = self.runner.run_main(method=method, url=url, data=None, header=header)
        return result


if __name__ == '__main__':
    from config.global_dict import temp_dict
    i = DomesticSeaApi(temp_dict)
    a = i.domestic_sea_save(**{"shippingInfo.consignee.addressCode":"测试",'referenceOrders.0.referenceOrderNo':13134567978945})
    # a = i.domestic_sea_submit(id=4522581089311580160)
    print(a)