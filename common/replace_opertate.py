import re,json,jsonpath
from config.get_conf import Conf
from util.operate_global import GlobalDict
from config.Log import Log

class ReplaceOperte:

    def __init__(self,dict):
        self.log = Log()
        self.global_dict = GlobalDict(dict)

    def replace_global_value(self,global_dict,result):
        '''
        :param global_dict: 将excel中的global写入全局字典中
        :param result:响应结果对应的值获取后存入全局字典中
        :return:
        '''
        if isinstance(global_dict,dict) and isinstance(result,dict):
            for key,value in global_dict.items():
                new_value = jsonpath.jsonpath(result,value)
                if not isinstance(new_value,bool):
                    new_value = jsonpath.jsonpath(result, value)[0]
                if new_value:
                    self.global_dict.set_dict(key,new_value)

    def replace_excel(self,params):
        '''
        :param params: 需要替换的内容
        :return: 返回替换后的内容
        '''
        self.log.debug(u'替换前的参数：%s'%params)
        new_params = params
        while re.search(r'\${#.+?}',new_params,re.M) or re.search(r'\${.+?}',new_params,re.M):
            #判断是否包含$#用于模糊查询替换
            if re.findall(r'\${#.+?}',new_params,re.M):
                for i in re.findall(r'\${#.+?}',new_params,re.M):
                    if re.search(r'\${#(.+?)}',i):
                        i = re.search(r'\${#(.+?)}',i).group(1)
                        self.log.debug(u'获取全局变量名：%s'%i)
                        new_value = ''
                        #判断在全局变量中能否找到对应的键
                        if self.global_dict.get_dict(i):
                            return_value = self.global_dict.get_dict(i)
                            self.log.debug(u'全局变量返回的的值：%s'%return_value)
                            new_value = return_value[0:len(return_value)-1]
                            self.log.debug(u'截取全局变量返回的值除最后一位：%s'%new_value)
                            #判断new_value类型是否为字符串类型
                            if isinstance(new_value,str):
                                new_key = '#'+i
                                self.global_dict.set_dict(new_key,new_value)
                                self.log.debug(u'新的键：%s和值：%s写入全局字典中用于预期结果调用'%(new_key,new_value))
                            else:
                                self.log.debug(u'%s为:%s' % (new_value,type(new_value)))
                        new_params = re.sub(r'\${#%s}'%i,new_value,new_params)
                    self.log.debug(u'替换后的参数为：%s'%new_params)
                # return new_params
            #判断是否包含$用于精准查询替换
            elif re.findall(r'\${(.+?)}',new_params,re.M):
                for i in re.findall(r'\${(.+?)}',new_params,re.M):
                    self.log.debug(u'获取全局变量名：%s' % i)
                    new_value = ''
                    if self.global_dict.get_dict(i):
                        new_value = self.global_dict.get_dict(i)
                        self.log.debug(u'全局变量返回的的值：%s' % new_value)
                    new_params = re.sub(r'\${%s}'%i,new_value,new_params)
                    self.log.debug(u'替换后的参数为：%s' % new_params)
                # return new_params
            #不用替换
            else:
                self.log.debug(u'未做任何替换的参数为：%s' % params)
        return new_params

    def replace_expect(self,params,result):
        '''
        断言
        :param params: excel中的expect
        :param result: 响应结果
        :return:
        '''
        temp_list = []

        for i in params:
            descript,expect,res = i     #描述，预期结果，实际结果
            self.log.debug('描述：%s,预期结果：%s，实际结果：%s'%(descript,expect,res))
            key = re.search(r'\$\.\.(.*)',res).group(1)
            if re.search(r'\${(.+?)}',expect):
                old_value = re.search(r'\${(.+?)}',expect).group(1)
                self.log.debug('获取预期结果的键为：%s'%old_value)
                new_value = self.global_dict.get_dict(old_value)
                self.log.debug('从全局字典中获取预期结果：%s'%new_value)
                res_value = jsonpath.jsonpath(result, res)
                if isinstance(res_value,list):
                    res_value = jsonpath.jsonpath(result,res)[0]
                    self.log.debug('实际结果：%s'%res_value)
                if descript == 'Equal':
                    self.log.info('预期结果的%s:%s，实际结果的%s:%s'%(key,new_value,key,res_value))
                    temp_list.append('self.assertEqual("%s","%s")'%(new_value,res_value))
                if descript == 'NotEqual':
                    self.log.info('预期结果的%s:%s，实际结果的%s:%s'%(key,new_value,key,res_value))
                    temp_list.append('self.assertNotEqual("%s","%s")'%(new_value,res_value))
                elif descript == 'In':
                    self.log.info('预期结果的%s:%s，实际结果的%s:%s' % (key, new_value, key, res_value))
                    temp_list.append('self.assertIn("%s","%s")' % (new_value, res_value))
                elif descript == 'NotIn':
                    self.log.info('预期结果的%s:%s，实际结果的%s:%s' % (key, new_value, key, res_value))
                    temp_list.append('self.assertNotIn("%s","%s")' % (new_value, res_value))

            else:
                res_value = jsonpath.jsonpath(result,res)
                if  isinstance(res_value,list):
                    res_value = jsonpath.jsonpath(result,res)[0]
                if descript == 'Equal':
                    self.log.info('预期结果的%s:%s，实际结果的%s:%s' % (key, expect, key, res_value))
                    temp_list.append('self.assertEqual("%s","%s")'%(expect,res_value))
                elif descript == 'NotEqual':
                    self.log.info('预期结果的%s:%s，实际结果的%s:%s' % (key, expect, key, res_value))
                    temp_list.append('self.assertNotEqual("%s","%s")'%(expect,res_value))
                elif descript == 'In':
                    self.log.info('预期结果的%s:%s，实际结果的%s:%s' % (key, expect, key, res_value))
                    temp_list.append('self.assertIn("%s","%s")'%(expect,res_value))
                elif descript == 'NotIn':
                    self.log.info('预期结果的%s:%s，实际结果的%s:%s' % (key, expect, key, res_value))
                    temp_list.append('self.assertNotIn("%s","%s")'%(expect,res_value))
        return temp_list


if __name__ == '__main__':
    from util.test_01 import b
    y = {'a':'13981754228','b':'测试'}
    x ="{'x':'${#a}','y':'${b}'}"
    r = ReplaceOperte(y)
    g = GlobalDict(y)

    z = r.replace_excel(x)
    print(z)


