
from config.get_conf import Conf
from runMain.run_main import RunMain

class BmsQueryDownloadApi:

    def __init__(self,dict):
        self.conf = Conf()
        self.basic_url = self.conf.get_value('request_url', 'url')
        environment_name = self.conf.is_url(self.basic_url)
        self.basic_dict = self.conf.get_yaml(
            self.conf.get_file_path('api_pack', 'api_config', 'bms_query_or_download_api_conf.yml'))
        self.runner = RunMain()
        self.token = dict.get('token')

    def bms_query(self,**kwargs):
        '''
        bms仓储查询
        :return:
        '''
        bms_query_dict = self.basic_dict.get('bms_query_params')
        url = self.basic_url + bms_query_dict.get('url')
        method = bms_query_dict.get('method')
        params = bms_query_dict.get('params')

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

    def bms_download(self,**kwargs):
        '''
        bms账单下载
        :param kwargs:
        :return:
        '''
        bms_download_dict = self.basic_dict.get('bms_download_params')
        url = self.basic_url + bms_download_dict.get('url')
        method = bms_download_dict.get('method')
        params = bms_download_dict.get('params')

        for i, j in kwargs.items():  # 获取跟进字典的键
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

            if isinstance(j, str):
                temp_str = temp_str + '="%s"' % j
            elif isinstance(j, int):
                temp_str = temp_str + '=%s' % j

            if temp_str != None:
                exec(temp_str)  # 更改params的值

        header = self.basic_dict.get('header')
        header['Authorization'] = '%s' % self.token
        result = self.runner.run_main(method=method, url=url, data=params, header=header)
        return result



if __name__ == '__main__':
    from config.global_dict import temp_dict
    bms = BmsQueryDownloadApi(temp_dict)
    # res = bms.bms_query(**{"month":12})
    res = bms.bms_download(**{"billNo":"RBL201911060844"})

