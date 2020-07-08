from config.get_conf import Conf
from util.compare_dict import Compare_dict
import json

conf = Conf()
cd = Compare_dict()

yaml_path = conf.get_file_path('config','ideas_cargowise_map.yml')

map_dict = conf.get_yaml(yaml_path).get('ideas')

ideas_path = conf.get_file_path('test_data','ideas.json')
demand_path = conf.get_file_path('test_data','shipment-deand.json')

with open(ideas_path,'r',encoding='utf-8') as load_f:
    ideas_dict = json.load(load_f)['4470056766015864832']

with open(demand_path,'r',encoding='utf-8') as load_f:
    demand_dict = json.load(load_f)['4470056766015864832']

# a  = {'a':'b','c':'d'}
#
# aa = {"a":11,"c":12,'d':[{"e":11},{"e":13}]}
# bb = {"aa":11,"d":12,'f':[{"f":11},{"b":13}]}
#
# aa_1 = cd.recursion_dict()(aa)
# bb_1 = cd.recursion_dict()(bb)
#
# aa_11 = cd.dict_replace_list(a,aa_1)
# bb_11 = cd.dict_replace_list(a,bb_1)
#
# print(aa_11.intersection(bb_11))

# print(aa_1)

ideas_1 = cd.recursion_dict()(ideas_dict)
demand_1 = cd.recursion_dict()(demand_dict)

ideas = cd.dict_replace_list(map_dict,ideas_1)
demand = cd.dict_replace_list(map_dict,demand_1)

# print(ideas.intersection(demand_1))

print(ideas.difference(demand))
# print(demand.difference(ideas))






