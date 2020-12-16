import re,json,jsonpath,random
from common.replace_kinds import ReplaceKinds
from util.operate_global import GlobalDict
from config.get_conf import Conf

class ReplaceOperte(ReplaceKinds):

    __conf = Conf()
    __assert_dict = __conf.get_yaml(__conf.get_file_path('config','assert_conf.yml'))

    def replace_global_value(self,global_dict,result,params=None):
        '''
        :param global_dict: 将excel中的global写入全局字典中
        :param result:响应结果对应的值获取后存入全局字典中
        :return:
        '''
        random_int = None
        if isinstance(global_dict,dict) and isinstance(result,dict) :
            for key,value in global_dict.items():
                # 获取json文件同一组的的不同参数
                if value.startswith('same_group_'):
                    value = value[11:]
                    new_value = jsonpath.jsonpath(result, value)
                    if not isinstance(new_value, bool):
                        # 获取jsonpath 列表的随机数
                        if random_int == None:
                            if len(new_value) == 1 :
                                random_int = 0
                                new_value = jsonpath.jsonpath(result, value)[random_int]

                            elif len(new_value) > 1:
                                random_int = random.randint(0, len(new_value) - 1)
                                new_value = jsonpath.jsonpath(result, value)[random_int]
                        else:
                            new_value = jsonpath.jsonpath(result, value)[random_int]

                    if new_value:
                        if isinstance(new_value, int):
                            self.global_dict.set_dict(key, str(new_value))
                        else:
                            self.global_dict.set_dict(key, new_value)

                #全局变量排除不想要的值
                elif '_exclusive' in value:
                    value,exclusive_list = value.split('_exclusive')
                    new_value = jsonpath.jsonpath(result, value)
                    if new_value:
                        new_value_set = set(new_value)
                        exclusive_set = set(eval(exclusive_list))

                        #将返回结果排除不要的值后的列表
                        difference_value_list = list(new_value_set.difference(exclusive_set))
                        new_value = random.choice(difference_value_list)

                        if isinstance(new_value, int):
                            self.global_dict.set_dict(key, str(new_value))
                        else:
                            self.global_dict.set_dict(key, new_value)


                #全局字典包含$返回结果查找有的值写入全局字典
                elif '$' in value:
                    new_value = jsonpath.jsonpath(result,value)
                    if not isinstance(new_value,bool):
                        #获取jsonpath 列表的随机数

                        if len(new_value) == 1:
                            new_value = jsonpath.jsonpath(result, value)[0]

                        elif len(new_value) > 1 :
                            new_value_len = random.randint(0, len(new_value) - 1)
                            new_value = jsonpath.jsonpath(result, value)[new_value_len]

                    if new_value:
                        if isinstance(new_value,int):
                            self.global_dict.set_dict(key,str(new_value))
                        else:
                            self.global_dict.set_dict(key, new_value)

                #将输入参数写入全局字典
                elif 'input_params' in value:
                    self.global_dict.set_dict(key,params)

                #自定义的值输入全局字典
                elif '$' not in value and 'input_params' not in value and 'same_group' not in value and '_exclusive' not in value:
                    self.global_dict.set_dict(key,value)

    def replace_excel(self,params):
        '''
        :param params: 需要替换的内容
        :return: 返回替换后的内容
        '''
        self.log.debug(u'替换前的参数：%s'%params)
        new_params = params

        #判断是否包含$#用于模糊查询替换
        data = self.fuzzy_replace(new_params)

        # 判断是否包含$@用于生成随机数查询替换
        data = self.random_replace(data)

        #判断是否包含$__attachment用于附件列表
        data = self.attachment_replace(data)

        # 判断是否包含$用于精准查询替换
        data = self.accurate_replace(data)
        return data

    def replace_expect(self, params, result):
        '''
        unittest断言
        :param params: excel中的expect
        :param result: 响应结果
        :return:
        '''
        temp_list = []
        unittest_assert_dict = self.__assert_dict.get('unittest') #获取断言配置文件中unittest的断言方法

        for i in params:
            descript, expect, res = i  # 描述，预期结果，实际结果
            self.log.debug('描述：%s,预期结果：%s，实际结果：%s' % (descript, expect, res))
            key = re.search(r'\$\.\.(.*)', res).group(1)
            if re.search(r'\${(.+?)}', expect):
                old_value = re.search(r'\${(.+?)}', expect).group(1)
                self.log.debug('获取预期结果的键为：%s' % old_value)
                new_value = self.global_dict.get_dict(old_value)
                self.log.debug('从全局字典中获取预期结果：%s' % new_value)
                res_value = jsonpath.jsonpath(result, res)
                if isinstance(res_value, list):
                    res_value = jsonpath.jsonpath(result, res)[0]
                    self.log.debug('实际结果：%s\n\n\n' % res_value)

                self.log.info('预期结果的%s:%s，实际结果的%s:%s' % (key, new_value, key, res_value))
                if descript == 'In' or descript == 'NotIn':
                    temp_list.append('%s ("%s","%s")' % (unittest_assert_dict.get(descript), new_value.lower(), res_value.lower()))
                else:
                    temp_list.append('%s ("%s","%s")' % (unittest_assert_dict.get(descript), new_value, res_value))

            else:
                res_value = jsonpath.jsonpath(result, res)
                if isinstance(res_value, list):
                    res_value = jsonpath.jsonpath(result, res)[0]

                self.log.info('预期结果的%s:%s，实际结果的%s:%s' % (key, expect, key, res_value))
                if descript == 'In' or descript == 'NotIn':
                    temp_list.append('%s ("%s","%s")' % (unittest_assert_dict.get(descript), expect.lower(), res_value.lower()))
                else:
                    temp_list.append('%s ("%s","%s")' % (unittest_assert_dict.get(descript), expect, res_value))
        return temp_list

    def replace_expect_pytest(self,params,result):
        '''
        pytest断言
        :param params: excel中的expect
        :param result: 响应结果
        :return:
        '''
        temp_list = []
        pytest_assert_dict = self.__assert_dict.get('pytest')  # 获取断言配置文件中pytest的断言方法

        for i in params:
            descript, expect, res = i  # 描述，预期结果，实际结果
            self.log.debug('描述：%s,预期结果：%s，实际结果：%s' % (descript, expect, res))
            key = re.search(r'\$\.\.(.*)', res).group(1)
            if re.search(r'\${(.+?)}', expect):
                old_value = re.search(r'\${(.+?)}', expect).group(1)
                self.log.debug('获取预期结果的键为：%s' % old_value)
                new_value = self.global_dict.get_dict(old_value)
                self.log.debug('从全局字典中获取预期结果：%s' % new_value)
                res_value = jsonpath.jsonpath(result, res)
                if isinstance(res_value, list):
                    res_value = jsonpath.jsonpath(result, res)[0]
                    self.log.debug('实际结果：%s' % res_value)

                self.log.info('预期结果的%s:%s，实际结果的%s:%s' % (key, new_value, key, res_value))
                if descript == 'In' or descript == 'NotIn':
                    temp_list.append('assert("%s"%s"%s")' % (new_value.lower(),pytest_assert_dict.get(descript), res_value.lower()))
                else:
                    temp_list.append('assert("%s"%s"%s")' % (new_value, pytest_assert_dict.get(descript), res_value))
            else:
                res_value = jsonpath.jsonpath(result, res)
                if isinstance(res_value, list):
                    res_value = jsonpath.jsonpath(result, res)[0]

                self.log.info('预期结果的%s:%s，实际结果的%s:%s' % (key, expect, key, res_value))
                if descript == 'In' or descript == 'NotIn':
                    temp_list.append('assert("%s"%s"%s")' % (expect.lower(),pytest_assert_dict.get(descript),res_value.lower()))
                else:
                    temp_list.append('assert("%s"%s"%s")' % (expect, pytest_assert_dict.get(descript), res_value))
        return temp_list



if __name__ == '__main__':
    m = {'mm':[{"id":"123456","name":"name01","sex":"男"},{"id":"6549721","name":"name02","sex":"女"},{"id":"456456789","name":"name03","sex":"未知"}]}
    y = {'d':'$..id_exclusive["123456",True,123,None]','b':'same_group_$..id','a':'same_group_$..name','c':'$..sex',}
    x ="{'x':$__attachment{internat_air},'y':'${b} ${@GBK}'}"
    tem_d = {}
    r = ReplaceOperte(tem_d)
    g = GlobalDict(tem_d)

    z = r.replace_global_value(y,m)

    print(tem_d.get('a'),tem_d.get('b'),tem_d.get('c'),tem_d.get('d'))
