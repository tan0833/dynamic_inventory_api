'''
获取data中的excel用例转换为列表用于参数化
'''
from util.operate_excel import Operate_excel
from config.get_conf import Conf
from itertools import chain

class ChainExcelData:

    def excel_case_list(self):
        '''
        将excel多个sheet的数据合并到一个大列表
        :return: 列表
        '''
        conf = Conf()
        d = []
        # 环境地址
        environment_url = conf.get_value('request_url', 'url')
        # 环境名称
        environment_name = conf.is_url(environment_url)
        # 读取yaml文件中需要执行的excel文件名和sheet名
        execute_case_name = conf.get_yaml(conf.get_file_path('config', 'excel_file.yml')).get('file_name')
        for project_name in execute_case_name:
            for key in project_name.keys():
                excel_name = project_name[key]
                if environment_name in excel_name.get('excel_name'):
                    excel_file_name = excel_name.get('excel_name')
                    sheet_list = excel_name.get('sheet_name')
                    for sheet in sheet_list:
                        if sheet == '登录':
                            res = Operate_excel(conf.get_file_path('data', excel_file_name), sheet)
                            login = res.excel_dict()
                            d.extend(login)
                        elif sheet == '基础数据':
                            res = Operate_excel(conf.get_file_path('data', excel_file_name), sheet)
                            d01 = res.excel_dict()
                            d.extend(d01)
                        else:
                            res = Operate_excel(conf.get_file_path('data', excel_file_name), sheet)
                            d02 = res.excel_dict()
                            d.extend(d02)

                elif 'UAT' not in excel_name.get('excel_name') and 'SIT' not in excel_name.get(
                        'excel_name') and 'DEV' not in excel_name.get('excel_name'):
                    excel_file_name = excel_name.get('excel_name')
                    sheet_list = excel_name.get('sheet_name')
                    for sheet in sheet_list:
                        res = Operate_excel(conf.get_file_path('data', excel_file_name), sheet)
                        d2 = res.excel_dict()
                        d.extend(d2)
        return d


    def excel_case_generator(self):
        '''
        将excel多个sheet的数据合并到一个大的生成器
        :return: 生成器
        '''
        conf = Conf()
        g = ([])
        # 环境地址
        environment_url = conf.get_value('request_url', 'url')
        # 环境名称
        environment_name = conf.is_url(environment_url)
        # 读取yaml文件中需要执行的excel文件名和sheet名
        execute_case_name = conf.get_yaml(conf.get_file_path('config', 'excel_file.yml')).get('file_name')
        for project_name in execute_case_name:
            for key in project_name.keys():
                excel_name = project_name[key]
                if environment_name in excel_name.get('excel_name'):
                    excel_file_name = excel_name.get('excel_name')
                    sheet_list = excel_name.get('sheet_name')
                    for sheet in sheet_list:
                        if sheet == '登录':
                            res = Operate_excel(conf.get_file_path('data', excel_file_name), sheet)
                            login = res.excel_dict_generator()
                            g=chain(g,login)
                        elif sheet == '基础数据':
                            res = Operate_excel(conf.get_file_path('data', excel_file_name), sheet)
                            d01 = res.excel_dict_generator()
                            g = chain(g,d01)
                        else:
                            res = Operate_excel(conf.get_file_path('data', excel_file_name), sheet)
                            d02 = res.excel_dict_generator()
                            g=chain(g,d02)

                elif 'UAT' not in excel_name.get('excel_name') and 'SIT' not in excel_name.get(
                        'excel_name') and 'DEV' not in excel_name.get('excel_name'):
                    excel_file_name = excel_name.get('excel_name')
                    sheet_list = excel_name.get('sheet_name')
                    for sheet in sheet_list:
                        res = Operate_excel(conf.get_file_path('data', excel_file_name), sheet)
                        d2 = res.excel_dict_generator()
                        g= chain(g,d2)
        return g


if __name__ == '__main__':

    for i in ChainExcelData().excel_case_generator():
        print(i)








