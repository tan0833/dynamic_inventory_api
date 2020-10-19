from configparser import ConfigParser
import os,yaml,json
from config.Log import Log
from ruamel import yaml as yml


class Conf:
    # cf = ConfigParser()
    # cf.read('D:/文档/测试/config/conf.ini')
    log = Log()

    def get_key_value(self,ini_value):
        '''获取键值对'''
        cf = ConfigParser()
        conf_ini = self.get_file_path('config','conf.ini')
        cf.read(conf_ini)
        return dict(cf.items(ini_value))

    def get_value(self,ini_key,ini_value):
        '''获取值'''
        cf = ConfigParser()
        conf_ini = self.get_file_path('config', 'conf.ini')
        cf.read(conf_ini)
        value = cf.get(ini_key,ini_value)
        # self.log.info('配置文件conf.ini中%s的值为:%s'%(ini_value,value))
        return value

    def get_file_path(self,*args):
        '''获取文件路径'''
        current_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_path = os.path.join(current_path,*args)
        # self.log.info('文件路径为：{}'.format(file_path))
        return file_path

    def is_url(self,url):
        '''
        判断url是uat还是sit
        :param url:
        :return:
        '''
        if 'sit' in url or 'j1' in url:
            return 'SIT'
        elif 'uat' in url or 'j2' in url:
            return 'UAT'
        elif 'dev' in url:
            return 'DEV'


    def get_yaml(self,yaml_file):
        '''
        将yaml文件转换为字典
        :param yaml_file: yaml文件
        :return:
        '''
        fp = open(yaml_file,encoding='utf-8')
        result = yaml.safe_load(fp)
        fp.close()
        return result

    def write_yaml(self,input_params,write_file):
        '''
        将字典写入ymal文件
        :param input_params: 输入字典参数
        :param write_file: 写入的ymal文件
        :return:
        '''
        fp = open(write_file, "w", encoding="utf-8")
        yml.dump(input_params,fp,Dumper=yml.RoundTripDumper)
        fp.close()

    def write_json(self,input_params,write_file):
        '''
        将字典写入json文件
        :param input_params: 字典参数
        :param write_file: 写入的json文件
        :return:
        '''
        json_str = json.dumps(input_params, indent=4)
        fp = open(write_file, "w", encoding="utf-8")
        fp.write(json_str)
        fp.close()


if __name__ == '__main__':
    c = Conf()
    x = c.get_file_path('api_pack','api_params','SIT','domestic_road_save_api_params.json')

    desired_caps = {
        'platformName': 'Android',
        'platformVersion': '8.0',
        'deviceName': 'A5RNW18316011440',
        'appPackage': 'com.tencent.mm',
        'appActivity': '.ui.LauncherUI',
        'automationName': 'Uiautomator2',
        'unicodeKeyboard': True,
        'resetKeyboard': True,
        'noReset': True,
        'chromeOptions': {'androidProcess': {"aa":12,"bb":[12,13]}}
    }
    b = c.write_json(desired_caps,x)
    print(b)
