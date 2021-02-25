from api_count.do_swagger import SwaggerApi
from api_count.write_coverage import calc_api_test_coverage


def api_count_probability(num):
    '''
    计算接口覆盖率
    :param num: 实际接口数量
    :return: /
    '''
    void_api_path = ['actuator', 'error']
    swagger_url = ['https://mpdev.jus-link.com/api/juslink-sccp-shipment-demand-app/v2/api-docs',
                       'https://mpdev.jus-link.com/api/juslink-sccp-shipment-demand-admin/v2/api-docs']

    api_count = SwaggerApi(swagger_url).get_api_total(void_api_path)

    calc_api_test_coverage(api_count,num)

if __name__ == '__main__':
    api_count_probability(90)
