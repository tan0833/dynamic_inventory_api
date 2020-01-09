import re
from util.operate_excel import Operate_excel
from config.get_conf import Conf

class ReplaceOperte:

    def __init__(self,file_name,sheet_name):
        self.conf = Conf()
        self.excel = Operate_excel(file_name,sheet_name)

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

    def replace_excel(self,params):
        pass



if __name__ == '__main__':
    r = ReplaceOperte(Conf().get_file_path('data','测试接口.xlsx'),0)
    print(r.excel_dict())
