'''
附件类型及基础数据的返回类型进行遍历
'''
from util.operate_global import GlobalDict
from runMain.run_main import RunMain
from util.operate_excel import WriteExcel
from util.operate_os import FindNewFile
import jsonpath,json,random
from config.get_conf import Conf
import requests

basic_url = Conf().get_value('request_url','url')


class ErgodicApi():

    def __init__(self,dict):
        self.runner = RunMain()
        self.new_excel_file = WriteExcel()
        self.get_new_excel_file = FindNewFile()
        self.test_file_path = Conf().get_file_path('test_file')
        self.token = dict.get('token')


    def attachment_ergodic(self,mode='TPM_SEA',is_internat=True):

        #附件接口输入参数
        method = 'POST'
        url = basic_url + '/api/juslink-sccp-shipment-demand-app/shipment-basic/file-types'
        header = {"Content-Type":"application/json",
                    "Authorization":self.token,
                    "clientId":"client",
                    "accept-language":"en-US"
                 }
        data = {
                "shippingMode":"%s"%mode,
                "transnationalShipment":is_internat
                }

        # result = requests.request(method=method,url=url,data=data,headers = header).text         #附件类型接口返回结果
        result = self.runner.run_main(method=method,url=url,header=header,data=data)
        res = jsonpath.jsonpath(result,'$..id')                                             #获取附件类型接口所有id列表
        attachments_list = []
        for i in res:
            self.new_excel_file.excel_write(i,i)                                              #生成包含附件类型excel
            new_file = self.get_new_excel_file.find_new_file(self.test_file_path)           #查找最新excel用于附件上传
            oss_method = 'POST'
            oss_url = basic_url + '/oss/objects'
            oss_header = {
                    "Authorization":self.token,
                    "clientId":"client",
                    "accept-language":"en-US"
                 }

            oss_data = {'fileName': '%d'%random.randint(10000000,99999999999),'bucketDirs': 'ShipmentDemand'}
            oss_file = [ ('file', open(new_file,'rb'))]
            #将最新的excel上传至文件服务返回的结果
            result1 = self.runner.run_main(method=oss_method,url=oss_url,header=oss_header,file=oss_file,data=oss_data)
            # result1 = requests.request(method=oss_method,url=oss_url,data=oss_data,headers = oss_header,files=oss_file).text
            file_id = jsonpath.jsonpath(result1,'$..data..id')[0]
            file_name = jsonpath.jsonpath(result1,'$..data..originName')[0]
            attachment_dict = {"name": file_name,"typeCode": i,"url": file_id}          #将文件类型，文件名称，文件id写入附件列表
            attachments_list.append(attachment_dict)
        self.get_new_excel_file.remove_file(self.test_file_path,4)                      #删除多余的excel文件，保留5个excel文件

        return str(attachments_list)



if __name__ == '__main__':
    dict_aa = {'token':'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0ZXJtaW5hbF90eXBlIjoid2ViIiwidXNlcl9uYW1lIjoiSFAiLCJzY29wZSI6WyJmb28iLCJyZWFkIiwid3JpdGUiXSwiYXBwbGljYXRpb25fY29kZSI6InNoaXBtZW50X2RlbWFuZF9hcHAiLCJleHAiOjE2MDA2ODczNjYsInVzZXJhY2NvdW50X2lkIjoiNDQyODM2MTM1MjM1MzY3MzIxNiIsImp0aSI6IjE1OWIxMTg2LTA3OGUtNGUwYi1iYjQ4LTM2YmNlNzY3NGUxMyIsImNsaWVudF9pZCI6InNoaXBtZW50X2RlbWFuZF9hcHAifQ.J4VOTPwxgi7cqdTbC51Xd_AuXljJZ4rwZcUFtbQ39c35IGeo3dMBjabVA1sbiIq5_egjojq92F7K_2YuvW9gHeCZaJSJs1YCgg5TUBGfR4eCQKLxqMzG5-czhq4VInftXISE1uMvmBBQqK3d6gt0DzGutQPbJFUj_FAAQWFd9wMvw_gvvKBX6ja3nzaHdiNZ1K0PnOJ-04IfNMdmdZKdxpwfu452GYSXgI8Gigf9Mj1dOspX1dedR9lFY3awdRkRSqOnt9hmUC-23WwT1HKlEUEyaNOw1JDvNhU9ZqIFbv5-8bJx4huvS0eQtkH9a9knfdQcBjbbJvGObUkerNvXOA'}
    e = ErgodicApi(dict_aa)
    test_attachment = {
        'method':'POST',
        'url':basic_url + '/juslink-sccp-shipment-demand-app/shipment-basic/file-types',
        'header':{"Content-Type":"application/json",
                    "Authorization":'token',
                    "clientId":"client",
                    "accept-language":"en-US"
                 },
        'data':{
                "shippingMode":"TPM_SEA",
                "transnationalShipment":True
                }
    }

    res = e.attachment_ergodic()
    print(str(res))
