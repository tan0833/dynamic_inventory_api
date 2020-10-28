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
#     login = Login()
#     token = json.loads(login.getTorken().text)['data']
#
    method = 'GET'
    url ='https://mpsit.jus-link.com/api/juslink-sccp-bill-query/bill-query/download'
    params = {"billNo":"RBL202004211784"}
    head = {
    "Authorization":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0ZXJtaW5hbF90eXBlIjoid2ViIiwidXNlcl9uYW1lIjoiSFAiLCJzY29wZSI6WyJmb28iLCJyZWFkIiwid3JpdGUiXSwiYXBwbGljYXRpb25fY29kZSI6InNoaXBtZW50X2RlbWFuZF9hcHAiLCJleHAiOjE2MDMzNjE5MDQsInVzZXJhY2NvdW50X2lkIjoiNDQyODM2MTM1MjM1MzY3MzIxNiIsImp0aSI6IjQ4ZDg0YjU5LTY5ODYtNGU3NC05ZGIwLTEzZGQzNmUyMTViMyIsImNsaWVudF9pZCI6InNoaXBtZW50X2RlbWFuZF9hcHAifQ.jUwlJtl7fQ5vIuT9sKn1G2zcDCFqD2-375imWafR4AheVPpBrgA_AInVS6oDRvFKDaW6VTGR3PFViovCLEbpuapaUN76bcUk5ZnhDsdXJCqIl4b-sqGzXcaXedLBSpBd7lQB4tno0GBfzXnl7b8CbK6XBMkMCiStMA8MNwkgiAV7jIvPk_bag5osE6ZdFDC3d_LB62Bt-0fAmLVNehkMvAhmweOkWvU3Ys7HbSWW62sXS8dJVzfyXQydctAhXOf5iclR59eCMdHOiuzMwMvBUbfo14CSXWutd7N0tP-xf6Vh9Ya2B3M_HkBV-a4TDGFZSFlBrhZe454Dm0-iqVreQA",
    "Content-Type":"application/json",
    "accept-language":"en-US",
    "clientId":"client"
}

    a = run.run_main(method,url,params,head)
    b = jsonpath.jsonpath(dict(a),'$..Content-Disposition')
    print(b)



