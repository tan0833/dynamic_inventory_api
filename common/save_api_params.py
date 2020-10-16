'''
8种运输模式保存的数据写入ymal文件，便于快速造数据
'''
from config.get_conf import Conf


class SaveApiParams:

    def __init__(self,dict):
        self.conf = Conf()
        self.basic_url = self.conf.get_value('request_url','url')


    def save_params(self):


        environment_name = self.conf.is_url(self.basic_url)
        file_dir_name = self.conf.get_file_path('api_pack','api_params',environment_name)
        print()