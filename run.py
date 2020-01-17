import unittest,time,datetime
# from Common.test import Test1
from BeautifulReport import BeautifulReport
from config.get_conf import Conf

#测试用例目录
case_dir = Conf().get_file_path('case')
#测试报告目录
report_dir = Conf().get_file_path('report')

date = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
testCase = unittest.defaultTestLoader.discover(start_dir=case_dir, pattern='test*.py')
print(testCase.countTestCases())

#执行测试用例
runner = BeautifulReport(testCase)
#生成测试报告
runner.report(description='客商门户查单接口测试报告', filename='客商门户查单接口测试报告' + date + '.html', report_dir=report_dir)