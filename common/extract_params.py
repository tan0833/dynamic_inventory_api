"""提取全局字典的参数"""

class ExtractParams:

    def __init__(self,global_dict):
        self.global_dict = global_dict

    def get_global_dict_value(self, global_value):
        replace_dict = {}
        if isinstance(global_value,dict):
            for key,value in global_value.items():
                new_value = self.global_dict.get(key)
                replace_dict[key] = new_value
        return replace_dict
