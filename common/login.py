import requests,traceback,json
from config.get_conf import Conf
from config.Log import Log


class Login:

    def __init__(self):
        self.log = Log()
        conf = Conf()
        self.url = conf.get_value('request_url', 'url')

    def login(self):
        '''登录成功，获取verificationCode'''
        try:
            request_url = self.url + '/authentication/signIn'
            payload = {
                      "clientId": "client",
                      "password": "Mima123!",
                      "redirectUrl": "string",
                      "route": "string",
                      "username": "MLB2-TEST01"
                    }

            payload = json.dumps(payload)
            headers = {
                'Content-Type': "application/json",
                'Cache-Control': "no-cache",
                'accept-encoding': "gzip, deflate",
                'content-length': "132",
                'Connection': "keep-alive",
                'cache-control': "no-cache"
            }

            response = requests.request("POST", request_url, data=payload, headers=headers)
        except Exception as e:
            self.log.error('登录接口未知错误：'+str(traceback.format_exc()))
        else:
            self.log.info('调用登录接口成功： ')
            return response

    def getTorken(self):
        '''
        获取torken
        :return:
        '''
        try:
            verificationCode = self.login().json()['data']['verificationCode']
            url = self.url+"/authentication/getToken/{}".format(verificationCode)

            headers = {
                'Content-Type': "application/json",
                'accept-encoding': "gzip, deflate",
                'Connection': "keep-alive",
            }

            response = requests.request("GET", url, headers=headers)
        except Exception as e:
            self.log.error('获取torken接口未知错误：'+str(traceback.format_exc()))
        else:
            self.log.info('获取torken接口成功： ')
            return response


if __name__ == '__main__':
    login = Login()
    r = login.getTorken()
    print(r.text)