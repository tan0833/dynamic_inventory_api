import re
from config.Log import Log
from util.operate_global import GlobalDict

class RegularReplace:

    def __init__(self,dict):
        self.log = Log()
        self.global_dict = GlobalDict(dict)

    def dim_replace(self,new_params):
        '''
        判断是否包含$#用于模糊查询替换
        :return:
        '''
        for i in re.findall(r'\${#.+?}', new_params, re.M):
            if re.search(r'\${#(.+?)}', i):
                i = re.search(r'\${#(.+?)}', i).group(1)
                self.log.debug(u'获取全局变量名：%s' % i)
                new_value = ''
                # 判断在全局变量中能否找到对应的键
                if self.global_dict.get_dict(i):
                    return_value = self.global_dict.get_dict(i)
                    self.log.debug(u'全局变量返回的的值：%s' % return_value)
                    new_value = return_value[0:len(return_value) - 1]
                    self.log.debug(u'截取全局变量返回的值除最后一位：%s' % new_value)
                    # 判断new_value类型是否为字符串类型
                    if isinstance(new_value, str):
                        new_key = '#' + i
                        self.global_dict.set_dict(new_key, new_value)
                        self.log.debug(u'新的键：%s和值：%s写入全局字典中用于预期结果调用' % (new_key, new_value))
                    else:
                        self.log.debug(u'%s为:%s' % (new_value, type(new_value)))
                new_params = re.sub(r'\${#%s}' % i, new_value, new_params)
            self.log.debug(u'替换后的参数为：%s' % new_params)


    def exact_replace(self,new_params):
        '''
        精准替换
        :param new_params:
        :return:
        '''
        for i in re.findall(r'\${(.+?)}', new_params, re.M):
            self.log.debug(u'获取全局变量名：%s' % i)
            new_value = ''
            if self.global_dict.get_dict(i):
                new_value = self.global_dict.get_dict(i)
                self.log.debug(u'全局变量返回的的值：%s' % new_value)
            new_params = re.sub(r'\${%s}' % i, new_value, new_params)
            self.log.debug(u'替换后的参数为：%s' % new_params)