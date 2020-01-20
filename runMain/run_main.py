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
        self.log.info(u'\n请求方法：%s\n请求地址：%s\n请求参数：%s\n请求头部：%s\n上传文件名称：%s'%(method,url,data,header,file))
        if method.upper() == 'GET':
            try:
                result = requests.request(method=method,url=url,params=data,headers = header)
                response =result.text
            except Exception as e:
                self.log.error('请求接口错误：\n'+str(traceback.format_exc()))
                raise e
        else:
            try:
                result = requests.request(method=method.upper(),url=url,data=json.dumps(data),headers = header)
                response = result.text
            except Exception as e:
                self.log.error('请求接口错误：\n'+str(traceback.format_exc()))
                raise e
        if response.startswith('{'):
            r = json.loads(response)
            response_result = json.dumps(r, sort_keys=True, indent=4, separators=(',', ':'),
                                         ensure_ascii=False)
            self.log.info('响应结果：\n%s'%response_result)
            return r
        elif not response.startswith('{') and result.status_code==200:
            header = dict(result.headers)
            response_result = json.dumps(header, sort_keys=True, indent=4, separators=(',', ':'),
                                         ensure_ascii=False)
            self.log.info('响应头部信息：\n%s' % response_result)
            return header
        else:
            self.log.info('响应结果为：%s'%response)
            return response


if __name__ == '__main__':
    run = RunMain()
    from common.login import Login
    import jsonpath
    login = Login()
    token = json.loads(login.getTorken().text)['data']

    method = 'POST'
    url ='https://j1.sccpcloud.com/api-gateway/dynamic-inventory-service/inventory/export-inventory-list'
    params = {
             "advancedQueryCriteria": {
              "mgtModes": [],
              "partNos": [],
              "statusFilterDate": 10,
              "stockStatusSet": [],
              "warehouseNames": []
             },
             "keyword": "117S0002"
            }
    head = {'Content-Type': 'application/json','Authorization': token,'clientId': 'client'}
    a = run.run_main(method,url,params,head)
    b = jsonpath.jsonpath(dict(a),'$..content-disposition')
    print(b)



