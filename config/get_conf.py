from configparser import ConfigParser
import os
from config.Log import Log

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

if __name__ == '__main__':
    c = Conf()
    x = c.get_file_path('usual_url','url')
    print(x)
