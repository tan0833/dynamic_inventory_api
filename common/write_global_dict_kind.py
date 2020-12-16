#写入全局字典的种类，用于后面组装
import jsonpath,random
from common.replace_kinds import ReplaceKinds


class GlobalDictKind(ReplaceKinds):

    def same_group_set_dict(self,global_dict,result):
        '''
        获取json文件同一组的的不同参数
        :param global_dict:
        :param result:
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


    def exclusive_set_dict(self,global_dict,result):
        '''
        全局变量排除不想要的值
        :param global_dict:
        :param result:
        :return:
        '''
        if isinstance(global_dict,dict) and isinstance(result,dict) :
            for key,value in global_dict.items():
                value, exclusive_list = value.split('_exclusive')
                new_value = jsonpath.jsonpath(result, value)
                if new_value:
                    new_value_set = set(new_value)
                    exclusive_set = set(eval(exclusive_list))

                    # 将返回结果排除不要的值后的列表
                    difference_value_list = list(new_value_set.difference(exclusive_set))
                    new_value = random.choice(difference_value_list)

                    if isinstance(new_value, int):
                        self.global_dict.set_dict(key, str(new_value))
                    else:
                        self.global_dict.set_dict(key, new_value)


