import requests,traceback,json
from config.Log import Log
import sys

class RunMain:

    def __init__(self):
        self.log = Log()

    def run_main(self,method,url,data,header,file=None):
        '''
        :param method:请求方法
        :param url:请求地址
        :param data:请求数据
        :param header:请求头部
        :param file:需上传文件
        :return:响应结果信息
        '''
        if isinstance(header,dict):
            header_result = json.dumps(header, sort_keys=True, indent=4, separators=(',', ':'),
                                         ensure_ascii=False)
        else:
            header_result = header

        if isinstance(data,dict):
            data_result = json.dumps(data, sort_keys=True, indent=4, separators=(',', ':'),
                                         ensure_ascii=False)
        else:
            data_result = data

        self.log.info(u'\n请求方法：%s\n请求地址：%s\n请求参数：%s\n请求头部：%s\n上传文件名称：%s\n'%(method,url,data_result,header_result,file))
        if method.upper() == 'GET':
            try:
                result = requests.request(method=method,url=url,params=data,headers = header)
                response =result.text
            except Exception as e:
                self.log.error('请求接口错误：\n'+str(traceback.format_exc()))
                raise e
        else:
            try:
                if isinstance(header,dict):
                    if 'application/json' in header.values() or 'application/json;charset=UTF-8' in header.values():
                        result = requests.request(method=method.upper(),url=url,json=data,headers = header,files=file)
                    else:
                        result = requests.request(method=method.upper(),url=url,data=data,headers = header,files=file)
                    response = result.text
                else:
                    result = requests.request(method=method.upper(),url=url,data=data,headers = header,files=file)
                    response = result.text
            except Exception as e:
                self.log.error('请求接口错误：\n'+str(traceback.format_exc()))
                raise e
        if response.startswith('{'):
            r = json.loads(response)
            response_result = json.dumps(r, sort_keys=True, indent=4, separators=(',', ':'),
                                         ensure_ascii=False)
            self.log.info('\n响应结果：%s\n'%response_result)
            return r
        elif not response.startswith('{') and result.status_code==200:
            header = dict(result.headers)
            response_result = json.dumps(header, sort_keys=True, indent=4, separators=(',', ':'),
                                         ensure_ascii=False)
            self.log.info('\n响应头部信息：%s\n' % response_result)
            return header
        else:
            self.log.info('\n响应结果为：%s\n'%response)
            return response


if __name__ == '__main__':
    run = RunMain()
#     from common.login import Login
    import jsonpath
    from config.get_conf import Conf
#     login = Login()
#     token = json.loads(login.getTorken().text)['data']
#
    method = 'POST'
    url ='https://mpdev.jus-link.com/api/oss/objects'
    params = {
    "bucketDirs":"ShipmentDemand",
    "fileName":"vo6PJmKV3V15"
}
    head = {
    "Authorization":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0ZXJtaW5hbF90eXBlIjoid2ViIiwidXNlcl9uYW1lIjoiSFAiLCJzY29wZSI6WyJmb28iLCJyZWFkIiwid3JpdGUiXSwiYXBwbGljYXRpb25fY29kZSI6InNoaXBtZW50X2RlbWFuZF9hcHAiLCJleHAiOjE2MTEwNjIzMDEsInVzZXJhY2NvdW50X2lkIjoiNDQzODU0NjI5MTc3MTY0NTk1MiIsImp0aSI6ImEzZmI1NzliLTk5ODYtNDY4YS04NWFkLTVhNmJhNmM3NDU4NCIsImNsaWVudF9pZCI6InNoaXBtZW50X2RlbWFuZF9hcHAifQ.AvyvZh240iuaSkWnp4XB4W5xFf90Y0EXTp-Br-nIIP27WUu3vVZz8f3WIlWIL-6oR-QBjJ8UO9K4y_HSjcGFPsQmRhHy1--oDUG2c_hjBJ7CfM-4XQNMwb6rcbGdjzeF_7J5HCVXnH92uqwNklZJTWQKEB1XbXvRQmBnvwLQOuCNBea1oqwipH4RNF04Zgnf8Be7o4FcTHJu1wYYDDEHRRU51OY_gLNL0opfAmcby6JBwuD-BNOk2gAv3cDWFsDG8cnmTLSMYPhzFsVJdmTXP7e4DYIpu8ERBg1xFKfNOfnhAXX2-Vv92npQuzXXApbcX18hIaJjn8ptn9XBHAOg_g",
    "accept-language":"en-US",
    "clientId":"client"
}
    file = [('file', open(Conf().get_file_path('data','运输下单测试用例-DEV.xlsx'),'rb'))]
    a = run.run_main(method,url,params,head,file=file)
    b = jsonpath.jsonpath(dict(a),'$..Content-Disposition')
    print(b)



