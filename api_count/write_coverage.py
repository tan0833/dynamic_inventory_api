
from config.Log import Log
from config.get_conf import Conf

# file_path = '项目路径下/swagger/swagger_info.txt'  # 在项目路径下新建文件夹swagger，并在里面创建swagger_info.txt文件
file_path = Conf().get_file_path('swagger','swagger_info.txt')
log = Log()

def calc_api_test_coverage(swagger_api_count, api_test_count):
    """
    计算接口测试覆盖率,并将结果写回swagger_info.txt
    :param swagger_api_count:  swagger接口总数
    :param api_test_count:   测试接口总数
    :return:  测试覆盖率
    """

    log.info(f'swagger接口总数：{swagger_api_count}')
    log.info(f'测试覆盖的接口总数：{api_test_count}')  # 根据自己情况看是否减掉登录的接口
    try:
        api_test_coverage = f'{(api_test_count / swagger_api_count) * 100:.2f}%'
        log.info(f'接口测试覆盖率：{api_test_coverage}')
    except ZeroDivisionError as e:
        log.error(f'swagger接口总数为 0')
        raise e
    else:
        with open(file_path, 'w+') as file:
            file.writelines(
                [f'swagger_api_count {swagger_api_count}\n',
                 f'api_test_count {api_test_count}\n',
                 f'api_test_coverage {api_test_coverage}'
                 ])

if __name__ == '__main__':
    calc_api_test_coverage(80,80)