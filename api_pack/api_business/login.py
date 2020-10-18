#登录相关操作

from config.get_conf import Conf
from runMain.run_main import RunMain
import jsonpath

class Login(object):

    def __init__(self):
        self.conf = Conf()
        self.basic_url = self.conf.get_value('request_url', 'url')
        self.basic_dict = self.conf.get_yaml(self.conf.get_file_path('api_pack', 'api_config', 'login_api.yml'))
        self.runner = RunMain()


    def login_business(self,username,password):
        '''
        登录流程
        :param username: 用户名
        :param password: 密码
        :return:
        '''
        login_result = self.login(username,password)
        token = jsonpath.jsonpath(login_result,'$..token')[0]
        verificationCode = jsonpath.jsonpath(login_result,'$..verificationCode')[0]
        identityId = self.identities(token=token)
        self.authentication(token=token,identityId=identityId)
        token_two = self.get_token(token=token,verificationCode=verificationCode)
        return token_two


    def login(self,username,password):
        '''
        登录
        :param username:用户名
        :param password:密码
        :return:
        '''
        login_dict = self.basic_dict.get('login')
        url = self.basic_url + login_dict.get('url')
        method = login_dict.get('method')
        header = login_dict.get('header')
        params = login_dict.get('params')
        params['username'] = '%s'%username
        params['password'] = '%s'% password
        result = self.runner.run_main(method = method,url = url,data=params,header=header)
        return result


    def identities(self,token):
        '''
        获取用户身份列表
        :return:
        '''
        identities_dict = self.basic_dict.get('identities')
        url = self.basic_url + identities_dict.get('url')
        method = identities_dict.get('method')
        header = self.basic_dict.get('header')
        header['Authorization'] = token
        result = self.runner.run_main(method=method,url=url,header=header,data={})
        identityId = jsonpath.jsonpath(result,'$..identityId')[0]
        return identityId

    def authentication(self,identityId,token):
        '''
        获取用户认证
        :param username: 用户名
        :param password: 密码
        :return:
        '''
        authentication_dict = self.basic_dict.get('authentication')
        url = self.basic_url + authentication_dict.get('url') + identityId
        method = authentication_dict.get('method')
        header = self.basic_dict.get('header')
        header['Authorization'] = token
        self.runner.run_main(method=method, url=url, header=header, data={})

    def get_token(self,verificationCode,token):
        '''
        获取token
        :param username: 用户名
        :param password: 密码
        :return:
        '''
        token_dict = self.basic_dict.get('token')
        url = self.basic_url + token_dict.get('url')
        method = token_dict.get('method')
        header = self.basic_dict.get('header')
        header['Authorization'] = token
        params = token_dict.get('params')
        params['code'] = verificationCode
        result = self.runner.run_main(method=method, url=url, header=header, data=params)
        token = jsonpath.jsonpath(result,'$..data')[0]
        return token




if __name__ == '__main__':
    l = Login()
    res = l.login_business('HP02','Jusda#123')
    print(res)