import re,json,jsonpath
from util.operate_excel import Operate_excel
from config.get_conf import Conf
from runMain.run_main import RunMain
from util.operate_global import GlobalDict

class ReplaceOperte:

    def __init__(self,file_name,sheet_name):
        self.conf = Conf()
        self.excel = Operate_excel(file_name,sheet_name)
        self.run = RunMain()
        self.global_dict = GlobalDict()

    def excel_dict(self):
        '''
        将excel英文标题作为键，每行内容作为值写入字典中，方便后续操作调用
        :return: 以列表形式返回
        '''
        title = []
        row_count = self.excel.get_rows()
        for i in range(1,row_count):
            key = self.excel.get_row_values(0)
            value = self.excel.get_row_values(i)
            th_dict = dict(zip(key,value))
            title.append(th_dict)
        return title

    def test_excel_params(self):
        '''
        用于测试的函数，方便获取excel的内容
        :return:
        '''
        li = self.excel_dict()[0]
        method = li['method']
        URL = self.conf.get_value('request_url','url')
        path = li['path']
        url = URL+path
        header = eval(li['header'])
        params = eval(li['params'])
        global_dict = eval(li['global'])
        # expect = eval(li['expect'])
        result = self.run.run_main(method,url,data=params,header=header)
        return global_dict,result

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
    r = ReplaceOperte(Conf().get_file_path('data','测试接口.xlsx'),0)
    a,b = r.test_excel_params()

    r.replace_global_value(a,b)

    c = r.excel_dict()[1]['params']
    d = r.replace_excel(c)
    print(d)
