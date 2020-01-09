import xlrd

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


if __name__ == '__main__':
    o = Operate_excel('D:\\文档\\运输可视化相关文档\\自动化\\克隆\\dynamic_inventory\\data\\动态库存接口测试用例.xlsx','登录')
    print(o.get_row_values(2))