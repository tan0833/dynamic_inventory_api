u'''
本页面将接口返回的数据以字典的形式存在全局字典中，方便后续调用
'''

from config.Log import Log
import traceback

class GlobalDict:

    __global_dict = {}

    def __init__(self):
        self.log = Log()

    def set_dict(self,key,value):
        self.__global_dict[key] = value

    def get_dict(self,key):
        try:
            value = self.__global_dict[key]
            return value
        except KeyError as e:
            self.log.error('输入的[%s]键不存在\n'%key)
        except Exception as e:
            self.log.error('未知错误：\n%s'%str(traceback.format_exc()))
            raise e

if __name__ == '__main__':

    a = GlobalDict()
    a.set_dict('c','12')
    b = a.get_dict('c')
    print(b)



