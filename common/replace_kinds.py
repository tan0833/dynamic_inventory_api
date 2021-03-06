import re,json,jsonpath,random
from config.get_conf import Conf
from util.operate_global import GlobalDict
from config.Log import Log
from util.create_random import CreateRandom
from common.regular_replace import RegularReplace
from common.ergodic_api import ErgodicApi

class ReplaceKinds:

    def __init__(self,dict):
        self.log = Log()
        self.global_dict = GlobalDict(dict)
        self.create_random = CreateRandom()
        self.replace_re = RegularReplace(dict)
        self.accurate = ErgodicApi(dict)

    def replace_random(self,random_value='GBK'):
        '''
        随机生成汉字，数字，特殊符号,公司，手机号写入全局字典
        :param random_value:
        :return:
        '''

        if random_value == 'GBK':
            company_name = self.create_random.random_create_company()
            self.global_dict.set_dict('GBK',company_name)

        elif random_value == 'INT':
            digit = self.create_random.random_create_digit()
            self.global_dict.set_dict('INT', str(digit))

        elif random_value == 'SYMBOL':
            symbol = self.create_random.random_create_symbol()
            self.global_dict.set_dict('SYMBOL',symbol)

        elif random_value == 'LETTER':
            letter = self.create_random.random_create_letter()
            self.global_dict.set_dict('LETTER',letter)

        elif random_value == 'CHAR':
            char_one = self.create_random.random_create_char()
            self.global_dict.set_dict('CHAR',char_one)

        elif random_value == 'PHONE':
            phone = self.create_random.random_create_mobile_phone()
            self.global_dict.set_dict('PHONE',phone)

        elif random_value == 'ENGLISH_COMPANY':
            phone = self.create_random.random_create_english_company()
            self.global_dict.set_dict('ENGLISH_COMPANY',phone)

        elif random_value == 'WORDS':
            phone = self.create_random.random_create_word()
            self.global_dict.set_dict('WORDS',phone)

        elif random_value == 'EMAIL':
            phone = self.create_random.random_create_email()
            self.global_dict.set_dict('EMAIL',phone)

    def fuzzy_replace(self, input_parmas):
        '''
        用户模糊替换，包含$#
        :param parmas:
        :return:
        '''
        search_fuzzy_parmas_list = re.findall(r'\${#.+?}', input_parmas, re.M)
        num = 0
        params = ''

        def common_replace(input_data):
            '''
            抽取公共部分未函数
            :param input_data:
            :return:
            '''
            data = input_data
            if re.search(r'\${#(.+?)}', data):
                i = re.search(r'\${#(.+?)}', data).group(1)
                self.log.debug(u'获取全局变量名：%s' % i)
                new_value = ''
                # 判断在全局变量中能否找到对应的键
                if self.global_dict.get_dict(i):
                    return_value = self.global_dict.get_dict(i)
                    self.log.debug(u'全局变量返回的的值：%s' % return_value)
                    # len_return_1 = random.randint(0, len(return_value))
                    # len_return_2 = random.randint(0, len(return_value))
                    # if len_return_1 < len_return_2:
                    #     new_value = return_value[len_return_1:len_return_2]
                    # elif len_return_1 > len_return_2:
                    #     new_value = return_value[len_return_2:len_return_1]
                    # elif len_return_1 == len_return_2:
                    #     new_value = return_value[0:len_return_1]
                    if len(return_value) == 0:
                        new_value = return_value
                    else:
                        new_value = return_value[0:len(return_value)-1]

                    self.log.debug(u'随机截取全局变量返回的值：%s' % new_value)
                    # 判断new_value类型是否为字符串类型
                    if isinstance(new_value, str):
                        new_key = '#' + i
                        self.global_dict.set_dict(new_key, new_value)
                        self.log.debug(u'新的键：%s和值：%s写入全局字典中用于预期结果调用' % (new_key, new_value))
                    else:
                        self.log.debug(u'%s为:%s' % (new_value, type(new_value)))
                params = re.sub(r'\${#%s}' % i, new_value, data)
                self.log.debug(u'替换后的参数为：%s' % params)
                return params
            else:
                return data

        # 如果没有匹配返回输入参数
        if len(search_fuzzy_parmas_list) == 0:
            params = input_parmas
        else:
            for j in search_fuzzy_parmas_list:
                # 第一个参数用输入的参数替换
                if re.search(r'\${#(.+?)}', input_parmas) and num == 0:
                    params = common_replace(input_parmas)
                    num = num + 1
                else:
                    # 第二个开始用第一个已替换的结果作为替换的入参
                    params = common_replace(params)
                    num = num + 1
        return params

    def random_replace(self,input_parmas):
        '''
        用户随机替换，包含$@
        :param input_parmas:
        :return:
        '''
        search_random_list = re.findall(r'\${@.+?}',input_parmas,re.M)
        num = 0
        params = ''

        def common_replace(input_data):
            '''
            将公共部分提取为函数
            :param input_data:
            :return:
            '''
            data = input_data
            if re.search(r'\${@(.+?)}', data):
                i = re.search(r'\${@(.+?)}', data).group(1)
                self.log.debug(u'获取全局变量名：%s' % i)
                self.replace_random(i)  # 生成随机数
                new_value = ''
                # 判断在全局变量中能否找到对应的键
                if self.global_dict.get_dict(i):
                    new_value = self.global_dict.get_dict(i)
                    self.log.debug(u'全局变量返回的的值：%s' % new_value)
                new_params = re.sub(r'\${@%s}' % i, new_value, data)
                self.log.debug(u'替换后的参数为：%s' % new_params)
                return new_params
            return data

        if len(search_random_list) == 0:
            params = input_parmas
        else:
            for j in search_random_list:
                if re.search(r'\${@(.+?)}', input_parmas) and num == 0:
                    params = common_replace(input_parmas)
                    num = num + 1
                else:
                    params = common_replace(params)
        return params

    def accurate_replace(self,input_params):
        '''
        用户精准替换，包含$
        :param input_params:
        :return:
        '''
        search_list = re.findall(r'\${.+?}',input_params,re.M)
        num = 0
        params = ''

        def common_replace(input_data):
            '''
            将重用部分抽取为公共函数
            :param input_data:
            :return:
            '''
            data = input_data
            if re.search(r'\${.+?}',data):
                i = re.search(r'\${(.+?)}',data).group(1)
                self.log.debug(u'获取全局变量名：%s' % i)
                new_value = ''
                if self.global_dict.get_dict(i):
                    new_value = self.global_dict.get_dict(i)
                    self.log.debug(u'全局变量返回的的值：%s' % new_value)
                new_params = re.sub(r'\${%s}' % i, new_value, data)
                self.log.debug(u'替换后的参数为：%s' % new_params)
                return new_params
            return data

        if len(search_list) == 0:
            params = input_params
        else:
            for j in search_list:
                if re.search(r'\${.+?}',input_params) and num == 0:
                    params = common_replace(input_params)
                    num = num + 1
                else:
                    params = common_replace(params)
        return params


    def mode_accessory(self,mode_params='internat_sea'):
        '''
        根据运输模式生成附件类型列表
        :param mode_params:
        :return:
        '''
        if mode_params == 'internat_sea':
            attachment_lists = self.accurate.attachment_ergodic('TPM_SEA',True)
            self.global_dict.set_dict('internat_sea',attachment_lists)
        elif mode_params == 'internat_air':
            attachment_lists = self.accurate.attachment_ergodic('TPM_AIR', True)
            self.global_dict.set_dict('internat_air', attachment_lists)
        elif mode_params == 'internat_rail':
            attachment_lists = self.accurate.attachment_ergodic('TPM_RAIL', True)
            self.global_dict.set_dict('internat_rail', attachment_lists)
        elif mode_params == 'internat_express':
            attachment_lists = self.accurate.attachment_ergodic('TPM_EXPRESS', True)
            self.global_dict.set_dict('internat_express', attachment_lists)
        elif mode_params == 'cn_sea':
            attachment_lists = self.accurate.attachment_ergodic('TPM_SEA', False)
            self.global_dict.set_dict('cn_sea', attachment_lists)
        elif mode_params == 'cn_air':
            attachment_lists = self.accurate.attachment_ergodic('TPM_AIR', False)
            self.global_dict.set_dict('cn_air', attachment_lists)
        elif mode_params == 'cn_road':
            attachment_lists = self.accurate.attachment_ergodic('TPM_ROAD', False)
            self.global_dict.set_dict('cn_road', attachment_lists)
        elif mode_params == 'cn_rail':
            attachment_lists = self.accurate.attachment_ergodic('TPM_RAIL', False)
            self.global_dict.set_dict('cn_rail', attachment_lists)
        elif mode_params == 'cn_express':
            attachment_lists = self.accurate.attachment_ergodic('TPM_EXPRESS', False)
            self.global_dict.set_dict('cn_express', attachment_lists)


    def attachment_replace(self,input_params):
        '''
        附件列表替换包含 如：${__attachment(internat_sea)}
        :param input_params:
        :return:
        '''

        search_attachment_list = re.findall(r'\$__attachment{.+?}', input_params, re.M)
        num = 0
        params = ''

        def common_replace(input_data):
            '''
            将重复代码抽出
            :param input_data:
            :return:
            '''
            data = input_data
            if re.search(r'\$__attachment{.+?}',data):
                i = re.search(r'\$__attachment{(.+?)}',data).group(1)
                self.log.debug(u'获取全局变量名：%s' % i)
                self.mode_accessory(i)  #根据运输模式的附件类型生成上传不重复的附件列表
                new_value = ''
                if self.global_dict.get_dict(i):
                    new_value = self.global_dict.get_dict(i)
                    self.log.debug(u'全局变量返回的的值：%s' % new_value)
                new_params = re.sub(r'\$__attachment{%s}' % i, new_value, data)
                self.log.debug(u'替换后的参数为：%s' % new_params)
                return new_params
            return data

        if len(search_attachment_list)==0:
            params = input_params
        else:
            for j in search_attachment_list:
                if re.search(r'\$__attachment{(.+?)}', input_params) and num == 0:
                    params = common_replace(input_params)
                    num = num + 1
                else:
                    params = common_replace(params)
        return params
