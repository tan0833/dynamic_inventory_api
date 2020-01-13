import re,json,jsonpath
from config.get_conf import Conf
from util.operate_global import GlobalDict
from config.Log import Log

class ReplaceOperte:

    def __init__(self,dict):
        self.log = Log()
        self.global_dict = GlobalDict(dict)

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
            new_value = ''
            if self.global_dict.get_dict(old_value):
                new_value = self.global_dict.get_dict(old_value)[0]
            new_params = re.sub(r'\${.+?}',new_value,params)
            return [new_params,new_value]
        else:
            return [params,'']

    def replace_expect(self,params,result):
        '''
        断言
        :param params: excel中的expect
        :param result: 响应结果
        :return:
        '''
        temp_list = []
        for i in params:
            descript,expect,res = i     #描述，预期结果，实际结果
            key = re.search(r'\$\.\.(.*)',res).group(1)
            if re.search(r'\${(.+?)}',expect):
                old_value = re.search(r'\${(.+?)}',expect).group(1)
                new_value = self.global_dict.get_dict(old_value)[0]
                res_value = jsonpath.jsonpath(result,res)[0]
                if descript == 'Equal':
                    self.log.info('预期结果的%s:%s，实际结果的%s:%s'%(key,new_value,key,res_value))
                    temp_list.append('self.assertEqual("%s","%s")'%(new_value,res_value))
            else:
                res_value = jsonpath.jsonpath(result,res)[0]
                if descript == 'Equal':
                    self.log.info('预期结果的%s:%s，实际结果的%s:%s' % (key, expect, key, res_value))
                    temp_list.append('self.assertEqual("%s","%s")'%(expect,res_value))
        return temp_list




if __name__ == '__main__':
    from util.operate_excel import Operate_excel
    from runMain.run_main import RunMain

    run = RunMain()
    rp = ReplaceOperte({})
    r = Operate_excel(Conf().get_file_path('data','测试接口.xlsx'),0)
    a = r.excel_dict()
    conf = Conf()
    for i in a:
        method = i['method']
        path =  rp.replace_excel(i['path'])[0]
        header = eval(i['header'])
        params = eval(rp.replace_excel(i['params'])[0])
        print(rp.replace_excel(i['params'])[1])
        global_d = eval(i['global'])
        url = conf.get_value('request_url','url') +path
        result = run.run_main(method,url,data=params,header=header)
        rp.replace_global_value(global_d,result)

        expect = i['expect']
        if expect.startswith('['):
            expect = eval(i['expect'])
            temp = rp.replace_expect(expect,result)
            print(temp)

