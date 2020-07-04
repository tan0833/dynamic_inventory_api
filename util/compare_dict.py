import json



class Compare_dict:


    __temp_set = set()

    def print_keyvalue_all(self,input_json):
        '''
        递归遍历json键用于比对两个json
        :param input_json:
        :return:
        '''
        if isinstance(input_json,dict):
            for key in input_json.keys():
                key_value = input_json.get(key)
                if isinstance(key_value,dict):
                    self.print_keyvalue_all(key_value)
                elif isinstance(key_value,list):
                    for json_array in key_value:
                        self.print_keyvalue_all(json_array)
                else:
                    self.__temp_set.add(str(key)+ " = " +str(key_value))

        elif isinstance(input_json,list):
            for input_json_array in input_json:
                self.print_keyvalue_all(input_json_array)

        return self.__temp_set

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

    # a = Compare_dict()
    # b = a.print_keyvalue_all(date_json)
    # print(b)

    a = {"1":"2","3":"4","5":"6"}
    b = '12345'

    def repl1(aa,bb):
        c = None
        for i in aa.keys():
            if i in bb:
                value = aa[i]
                c = bb.replace(i,value)
        return c

    c = repl1(a,b)
    print(c)
