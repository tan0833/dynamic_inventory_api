import re,json,jsonpath,random
from common.replace_kinds import ReplaceKinds
from util.operate_global import GlobalDict


class ReplaceOperte(ReplaceKinds):


    def replace_global_value(self,global_dict,result,params=None):
        '''
        :param global_dict: 将excel中的global写入全局字典中
        :param result:响应结果对应的值获取后存入全局字典中
        :return:
        '''
        if isinstance(global_dict,dict) and isinstance(result,dict) :
            for key,value in global_dict.items():
                #全局字典包含$返回结果查找有的值写入全局字典
                if '$' in value:
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
                elif '$' not in value and 'input_params' not in value:
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
                    self.log.debug('实际结果：%s\n\n\n'%res_value)
                if descript == 'Equal':
                    self.log.info('预期结果的%s:%s，实际结果的%s:%s\n\n\n'%(key,new_value,key,res_value))
                    temp_list.append('self.assertEqual("%s","%s")'%(new_value,res_value))
                if descript == 'NotEqual':
                    self.log.info('预期结果的%s:%s，实际结果的%s:%s\n\n\n'%(key,new_value,key,res_value))
                    temp_list.append('self.assertNotEqual("%s","%s")'%(new_value,res_value))
                elif descript == 'In':
                    self.log.info('预期结果的%s:%s，实际结果的%s:%s\n\n\n' % (key, new_value, key, res_value))
                    temp_list.append('self.assertIn("%s","%s")' % (new_value, res_value))
                elif descript == 'NotIn':
                    self.log.info('预期结果的%s:%s，实际结果的%s:%s\n\n\n' % (key, new_value, key, res_value))
                    temp_list.append('self.assertNotIn("%s","%s")' % (new_value, res_value))

            else:
                res_value = jsonpath.jsonpath(result,res)
                if  isinstance(res_value,list):
                    res_value = jsonpath.jsonpath(result,res)[0]
                if descript == 'Equal':
                    self.log.info('预期结果的%s:%s，实际结果的%s:%s\n\n\n' % (key, expect, key, res_value))
                    temp_list.append('self.assertEqual("%s","%s")'%(expect,res_value))
                elif descript == 'NotEqual':
                    self.log.info('预期结果的%s:%s，实际结果的%s:%s\n\n\n' % (key, expect, key, res_value))
                    temp_list.append('self.assertNotEqual("%s","%s")'%(expect,res_value))
                elif descript == 'In':
                    self.log.info('预期结果的%s:%s，实际结果的%s:%s\n\n\n' % (key, expect, key, res_value))
                    temp_list.append('self.assertIn("%s","%s")'%(expect,res_value))
                elif descript == 'NotIn':
                    self.log.info('预期结果的%s:%s，实际结果的%s:%s\n\n\n' % (key, expect, key, res_value))
                    temp_list.append('self.assertNotIn("%s","%s")'%(expect,res_value))
        return temp_list


if __name__ == '__main__':
    m = {"aa":"123456"}
    y = {'a':'13981754228','b':'input_params'}
    x ="{'x':$__attachment{internat_air},'y':'${b} ${@GBK}'}"
    r = ReplaceOperte(y)
    g = GlobalDict(y)

    z = r.replace_global_value(y,y,m)

    print(y)
