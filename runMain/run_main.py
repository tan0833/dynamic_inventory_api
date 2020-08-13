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

        self.log.info(u'\n请求方法：%s\n请求地址：%s\n请求参数：%s\n请求头部：%s\n上传文件名称：%s'%(method,url,data_result,header_result,file))
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
    method = 'POST'
    url ='https://mpsit.jus-link.com/api/juslink-sccp-shipment-demand-app/shipment-demand/domestic-rail/withdraw/4487020151668707328'
    params = {}
    head = {
    "Authorization":"eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0ZXJtaW5hbF90eXBlIjoid2ViIiwidXNlcl9uYW1lIjoiSFAwMiIsInNjb3BlIjpbInJlYWQiLCJ3cml0ZSIsImZvbyJdLCJhcHBsaWNhdGlvbl9jb2RlIjoiaG9tZSIsImV4cCI6MTU5NjEzNTYyOCwidXNlcmFjY291bnRfaWQiOiI0NDc1NjA2NjI4MjY0OTc2Mzg0IiwianRpIjoiMWM2NjMxYjItM2NmOS00YTU4LWIzOGUtOGJiODE4OGNjMDllIiwiY2xpZW50X2lkIjoiaG9tZSJ9.ARxzlWyh5GDlPXR8dZ8rZXPDxiDLaofl2hZQFsaPoKAdz-jJySV0o0IjiqI-DGVzc2m4RPSgJvvSmDS3C8C4VoeAbtgONGhbIBSxfD7V9U087kMMrxc-HqM5g4ZeL-ciFTwV5H37tYr1qhUh3-4v5rYSd5MWj13AxltW_G1fp-3rHrIIrD5JlSXKxnyfjDfQYgNHxYoONFLfx89yPZqjEVc4UDRzB33lVgBE9POerOLcjcv9i1ZwfWopFykh2xYMC_lG_xYe8Ih4eZKfmPNBz9vE29UaIgwqK_1y-0xAA1zP-Upeuqqc4kar6ILPO0E-nPPNCqV7IOLtwatQMyhnpw",
    "Content-Type":"application/json",
    "accept-language":"en-US",
    "clientId":"client"
}

    a = run.run_main(method,url,params,head)
    b = jsonpath.jsonpath(dict(a),'$..content-disposition')
    print(b)



