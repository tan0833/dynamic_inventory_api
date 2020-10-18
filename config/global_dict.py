#定义全局字典,方便测试时统一调用
from api_pack.api_business.login import Login


token = Login().login_business('HP02','Jusda#123')
temp_dict = {'token':''}
temp_dict['token'] = token


temp_list = []