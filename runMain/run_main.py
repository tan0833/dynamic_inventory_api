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
#     from common.login import Login
    import jsonpath
#     login = Login()
#     token = json.loads(login.getTorken().text)['data']
#
    method = 'GET'
    url ='https://j2.sccpcloud.com/api-gateway/waybill-query-app/waybill/detail/document'
    params = {'resourceCode': '2700b4f5e1c7e69b0836b1fecb2d06addb4c11754862de418b8e48fbcbe8f94a8e041b9aa1c65b641cd005835f10e627cb72f29519d19304d8cfd8c74aae24bd661b14badfd6d84764f956155245caf034331c758fa8c3b47cde3953027aba72e89a97bc9cc1314b59673adb43fe1a61afe7dacbf409c6833debd1011eb0dd0030ddedc3deba4cbddf914bbd9bf87c83'}
    head = {'Content-Type': 'application/x-www-form-urlencoded', 'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0ZXJtaW5hbF90eXBlIjoid2ViIiwidXNlcl9uYW1lIjoiV1laIiwic2NvcGUiOlsicmVhZCIsIndyaXRlIiwiZm9vIl0sImFwcGxpY2F0aW9uX2NvZGUiOiJob21lIiwiZXhwIjoxNTg4ODUyMjU2LCJ1c2VyYWNjb3VudF9pZCI6IjQ0MTk0OTQ1ODk5MzgzMzU3NDQiLCJqdGkiOiIwYmZhMTQzMC1lMGMzLTRiY2QtYmE1Ni1kZjY2ZGM1NTQ5NjEiLCJjbGllbnRfaWQiOiJob21lIn0.j19CjqevObuabK64QLWbzzEqtjuz61Na7xJArF18DMjBG57MhgjBtwuQEuqnf4VD5vwKxA5JqNdt1-HhAXanfNK8kZRLYTPPYkYsu2NOgG198FTk0z0s737gFKj21xMT5mbix_6hpYbv6S-xNdyfO8cN9P5u5N3lgyYHV0KE86bHY3Dijg8CUiSpiNTJW4bsC4EVkMqSLFSUiwnXkgYjOU2Gf6efI-gDwMdL4gVOQSvB2bsKJNOhKVugyab1eQqdnYjW9SPUKzUOcRFbgEZ3EzDZZVUEC72uMgToBzbhuu4F2Dgyi34GX-wMB94CHoIDiW1vtv30wkzZgS4uK35XjA', 'clientId': 'client'}
    a = run.run_main(method,url,params,head)
    b = jsonpath.jsonpath(dict(a),'$..content-disposition')
    print(b)



