import unittest,time,datetime
from BeautifulReport import BeautifulReport
from config.get_conf import Conf

#测试用例目录
case_dir = Conf().get_file_path('case')
#测试报告目录
report_dir = Conf().get_file_path('report')
#环境地址
url = Conf().get_value('request_url','url')
#环境名称
environment_name = Conf().is_url(url)

date = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
testCase = unittest.defaultTestLoader.discover(start_dir=case_dir, pattern='test*.py')
print(testCase.countTestCases())

#执行测试用例
runner = BeautifulReport(testCase)
# #生成测试报告
runner.report(description='运输下单%s接口测试报告'%environment_name, filename='运输下单%s接口测试报告'%environment_name + date + '.html', report_dir=report_dir)
