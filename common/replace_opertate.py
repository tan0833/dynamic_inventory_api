import re,json,jsonpath
from config.get_conf import Conf
from runMain.run_main import RunMain
from util.operate_global import GlobalDict

class ReplaceOperte:

    def __init__(self):

        self.global_dict = GlobalDict()

    def replace_global_value(self,global_dict,result):
        '''
        :param global_dict: 将excel中的global写入全局字典中
        :param result:响应结果对应的值获取后存入全局字典中
        :return:
        '''
        if isinstance(global_dict,dict) and isinstance(result,dict):
            for key,value in global_dict.items():
                new_value = jsonpath.jsonpath(result,value)
                if new_value:
                    self.global_dict.set_dict(key,new_value)

    def replace_excel(self,params):
        '''
        :param params: 需要替换的内容
        :return: 返回替换后的内容
        '''
        while re.search(r'\${(.+?)}',params):
            old_value = re.search(r'\${(.+?)}', params).group(1)
            new_value = None
            if self.global_dict.get_dict(old_value):
                new_value = self.global_dict.get_dict(old_value)[0]
            new_params = re.sub(r'\${.+?}',new_value,params)
            return new_params
        else:
            return params




if __name__ == '__main__':
    from util.operate_excel import Operate_excel
    rp = ReplaceOperte()
    r = Operate_excel(Conf().get_file_path('data','测试接口.xlsx'),0)
    a = r.excel_dict()

    for i in a:
        method = i['method']
        path =  i['path']
        header = i['header']
        params = i['parmms']
        global_d = i['global']




