import unittest,time,datetime
from BeautifulReport import BeautifulReport
from config.get_conf import Conf
from api_count.api_count_main import api_count_probability

#测试用例目录
case_dir = Conf().get_file_path('case','Test_Api')
# case_dir = Conf().get_file_path('case','Test_Flow')

#测试报告目录
report_dir = Conf().get_file_path('report')
#环境地址
url = Conf().get_value('request_url','url')
#环境名称
environment_name = Conf().is_url(url)

date = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
testCase = unittest.defaultTestLoader.discover(start_dir=case_dir, pattern='test*.py')

#打印用例数
print(testCase.countTestCases())

#实际接口数量
api_count_probability(81)


#执行测试用例
runner = BeautifulReport(testCase)
#生成测试报告
runner.report(description='%s运输下单V2.6.0接口测试报告'%environment_name, filename='%s运输下单V2.6.0接口测试报告'%environment_name + date + '.html', report_dir=report_dir)
# runner.report(description='%s运输下单基础数据遍历接口测试报告'%environment_name, filename='%s运输下单基础数据遍历接口测试报告'%environment_name + date + '.html', report_dir=report_dir)

