import datetime

import xlrd
import xlwt
from config.get_conf import Conf

class Operate_excel:

    def __init__(self,excel_file,sheet_name):
        self.excel = xlrd.open_workbook(excel_file)
        if type(sheet_name)==int:
            self.sheet = self.excel.sheet_by_index(sheet_name)
        else:
            self.sheet = self.excel.sheet_by_name(sheet_name)


    def get_rows(self):
        '''获取总行数'''
        return self.sheet.nrows

    def get_cols(self):
        '''获取总列数'''
        return self.sheet.ncols

    def get_row_values(self,row):
        '''获取整行值'''
        return self.sheet.row_values(row)

    def get_col_values(self,col):
        '''获取整列值'''
        return self.sheet.col_values(col)

    def get_cell_value(self,row,col):
        '''获取单元格值'''
        return self.sheet.cell_value(row,col)

    def close(self):
        '''关闭Excel'''
        self.excel.close()

    def excel_dict(self):
        '''
        将excel英文标题作为键，每行内容作为值写入字典中，方便后续操作调用
        :return: 以列表形式返回
        '''
        title = []
        row_count = self.get_rows()
        for i in range(1,row_count):
            key = self.get_row_values(0)
            value = self.get_row_values(i)
            th_dict = dict(zip(key,value))
            title.append(th_dict)
        return title

class WriteExcel:

    def excel_write(self,excle_content,file_name):
        '''
        生成随机excel文件
        :return:
        '''
        time_stamp = '{0:%Y-%m-%d %H_%M_%S}'.format(datetime.datetime.now())
        test_dir = Conf().get_file_path('test_file', '%s_%s.xlsx'%(file_name,time_stamp))
        # 创建excel文件
        filename = xlwt.Workbook(encoding="utf-8")
        # 给工作表命名，test
        sheet = filename.add_sheet("test")
        # 写入内容，第4行第3列写入excle_content
        sheet.write(1, 1, excle_content)
        # 指定存储路径，如果当前路径存在同名文件，会覆盖掉同名文件
        filename.save(test_dir)




if __name__ == '__main__':
    # o = Operate_excel('D:\\文档\\运输可视化相关文档\\自动化\\克隆\\dynamic_inventory\\data\\动态库存接口测试用例.xlsx','登录')
    # print(o.get_row_values(2))


    a = WriteExcel()
    a.excel_write('asdfasdfas','')
