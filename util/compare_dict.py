import json,jsonpath



class Compare_dict:

    def src_dest_equal(self,src_dict,dest_dict,map_dict):
        '''
        判断两个字典对应映射字段值是否相同
        :param src_dict: 第一个
        :param dest_dict: 第二个
        :param map_dict: 映射字典
        :return: 将相同和不同的分类
        '''
        equal_list = []
        not_equal_list = []
        if isinstance(src_dict,dict) and isinstance(dest_dict,dict) :
            for key in map_dict.keys():
                src_key,dest_key = map_dict.get(key)
                src_value = jsonpath.jsonpath(src_dict,'$..%s'%src_key)
                dest_value = jsonpath.jsonpath(dest_dict,'$..%s'%dest_key)
                if src_value == dest_value:
                    temp_dict01 = {}
                    temp_dict = {}
                    temp_dict01[src_key] = src_value
                    temp_dict01[dest_key] = dest_value
                    temp_dict[key] = temp_dict01
                    equal_list.append(temp_dict)
                else:
                    temp_dc = {}
                    temp_d01 = {}
                    temp_dc[src_key] = src_value
                    temp_dc[dest_key] = dest_value
                    temp_d01[key]=temp_dc
                    not_equal_list.append(temp_d01)
        return {'equal':equal_list,'not_equal':not_equal_list}


    def recursion_dict(self):
        __temp_list = []

        def print_keyvalue_all(input_json):
            '''
            递归遍历json键用于比对两个json
            :param input_json:
            :return:
            '''
            if isinstance(input_json,dict):
                for key in input_json.keys():
                    key_value = input_json.get(key)
                    if isinstance(key_value,dict):
                        print_keyvalue_all(key_value)
                    elif isinstance(key_value,list):
                        for json_array in key_value:
                            print_keyvalue_all(json_array)
                    else:
                        __temp_list.append(str(key)+ " = " +str(key_value))

            elif isinstance(input_json,list):
                for input_json_array in input_json:
                    print_keyvalue_all(input_json_array)

            return __temp_list
        return print_keyvalue_all


    def dict_replace_list(self,dict_value,list_value):
        '''
        列表中的元素包含字典的key替换为value
        :param dict_value:用于映射的字典
        :param list_value:需要被替换的列表
        :return:集合方式返回
        '''
        d = list_value
        for i in dict_value.keys():
            for j in range(len(d)):
                if i in d[j]:
                    d[j] = d[j].replace(i, dict_value.get(i))
        d = set(d)
        return d

if __name__ == '__main__':
    # json文件发送形式
    SendRegisterVerificationCodejson_txt = """
    {
        "menus": [{
            "key": "测试1",
            "type": "Channel"
        }, {
            "key": "测试2"
        }, {
            "key": "测试3",
            "type": "Channel"
        }],
        "test":"12",
        "test01":{"a":1,"b":2}
    }
    """
    date_json = json.loads(SendRegisterVerificationCodejson_txt)

    a = Compare_dict()
    # b = a.print_keyvalue_all(date_json)
    a01 = {'a': ['a','aa'], 'b':['c','d'],'c':['e','f'],'d':['f','b'] }

    aa = {"a": 11, "c": 12, 'd': [{"e": 11}, {"f": 13}]}
    bb = {"aa": 11, "d": 12, 'f': [{"f": 12}, {"b": 13}]}

    aa_1 = a.recursion_dict()
    bb_1 = a.recursion_dict()

    print(aa_1(aa))
    print(bb_1(bb))

    c = {"key":"value","3":"4","5":"6"}

    d = a.src_dest_equal(aa,bb,a01)
    print(d)







