'''
附件类型及基础数据的返回类型进行遍历
'''
from util.operate_global import GlobalDict
from runMain.run_main import RunMain
from util.operate_excel import WriteExcel
from util.operate_os import FindNewFile
import jsonpath,json
from config.get_conf import Conf
from config.global_dict import temp_dict

basic_url = Conf().get_value('request_url','url')
token = GlobalDict(temp_dict).get_dict('token')


class ErgodicApi:

    def __init__(self):
        self.runner = RunMain()
        self.new_excel_file = WriteExcel()
        self.get_new_excel_file = FindNewFile()
        self.test_file_path = Conf().get_file_path('test_file')


    def attachment_ergodic(self,attachment_dict):

        #附件接口输入参数
        method ,url,header,data= attachment_dict.get('method'),attachment_dict.get('url'),attachment_dict.get('header'),attachment_dict.get('data')
        result = self.runner.run_main(method=method,url=url,header=header,data=data)
        res = jsonpath.jsonpath(result,'$..id')
        attachments_list = []
        for i in res:
            self.new_excel_file.excel_write(i)
            new_file = self.get_new_excel_file.find_new_file(self.test_file_path)
            oss_method = 'POST'
            oss_url = basic_url + '/oss/objects'
            oss_header = {
                    "Authorization":token,
                    "clientId":"client",
                    "accept-language":"en-US"
                 }
            oss_data = {'fileName': '%d'%random.randint(10000,99999),'bucketDirs': 'ShipmentDemand'}
            oss_file = [ ('file', open(new_file,'rb'))]
            result1 = self.runner.run_main(method=oss_method,url=oss_url,header=oss_header,file=oss_file,data=oss_data)

            file_id = jsonpath.jsonpath(result1,'$..data..id')
            file_name = jsonpath.jsonpath(result1,'$..data..originName')
            attachment_dict = {"name": file_name,"typeCode": i,"url": file_id}
            attachments_list.append(attachment_dict)

        return str(attachments_list)



if __name__ == '__main__':
    import random
    e = ErgodicApi()
    test_attachment = {
        'method':'POST',
        'url':basic_url + '/juslink-sccp-shipment-demand-app/shipment-basic/file-types',
        'header':{"Content-Type":"application/json",
                    "Authorization":token,
                    "clientId":"client",
                    "accept-language":"en-US"
                 },
        'data':{
                "shippingMode":"TPM_SEA",
                "transnationalShipment":True
                }
    }

    oss_dict = {
        'oss_method':'POST',
        'oss_url':basic_url + '/oss/objects',
        'oss_header':{
                    "Authorization":token,
                    "clientId":"client",
                    "accept-language":"en-US"
                 },
        'oss_data':{'fileName': '%d'%random.randint(10000,99999),
                    'bucketDirs': 'ShipmentDemand'},
        'oss_file':[  ('file', open(Conf().get_file_path('data','运输下单常用sql.txt'),'rb'))]
    }
    res = e.attachment_ergodic(test_attachment)
    print(str(res))
