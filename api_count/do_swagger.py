# -*- encoding: utf-8 -*-

from config.Log import Log
import requests
from jsonpath import jsonpath

# 无效的接口地址
void_api_path = ['actuator', 'error']
log = Log()

class SwaggerApi:

    def __init__(self, url_list):
        self.url_list = url_list

    def get_api_url(self):
        """
        获取swagger json地址列表
        :return:
        """
        if isinstance(self.url_list, list):
            api_url = self.url_list
        else:
            log.error('swagger地址信息必须是列表')
            raise TypeError
        return api_url

    def get_api_total(self, void_path):
        """
        :param void_path: 无效的接口关键字   格式： [actuator]
                          例如：/actuator/health   /actuator/health/{component}  无效关键字为根路劲下的第一个目录 actuator
        :return: 返回swagger接口总数
        """
        api_path_list = []
        for item in self.get_api_url():
            response = requests.get(item).json()  # 可以换成自己封装的get请求
            api_info = response['paths'].items()
            for k, v in api_info:
                if k.split('/')[1] not in void_path:  # 接口是否有效
                    if not jsonpath(v, '$..deprecated')[0]:  # 接口是否被弃用
                        api_path_list.append(k)
        return len(api_path_list)


if __name__ == '__main__':
    swagger_url = ['https://mpsit.jus-link.com/api/juslink-sccp-shipment-demand-app/v2/api-docs',
                   'https://mpdev.jus-link.com/api/juslink-sccp-shipment-demand-admin/v2/api-docs']
    r = SwaggerApi(swagger_url).get_api_total(void_api_path)
    print(r)
