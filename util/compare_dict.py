import json



class Compare_dict:

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
    a01 = {'a': 'b', 'c': 'd'}

    aa = {"a": 11, "c": 12, 'd': [{"e": 11}, {"e": 13}]}
    bb = {"aa": 11, "d": 12, 'f': [{"f": 11}, {"b": 13}]}

    aa_1 = a.recursion_dict()
    bb_1 = a.recursion_dict()

    print(aa_1(aa))
    print(bb_1(bb))

    c = {"key":"value","3":"4","5":"6"}

    # d = a.dict_replace_list(c,c)
    # print(d)





