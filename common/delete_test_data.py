#删除测试数据
from config.get_conf import Conf
from util.operate_postgresql import OperarePostgresql
from config.Log import Log
import traceback


class DeleteTestData:

    def __init__(self,global_dict):
        self.conf = Conf()
        self.log = Log()
        self.global_dict = global_dict
        self.basic_url = self.conf.get_value('request_url','url')
        self.environment_name = self.conf.is_url(self.basic_url)
        self.database_dict = self.conf.get_yaml(self.conf.get_file_path('config','database_conf.yml'))
        self.delete_data_key_dict = self.conf.get_yaml(self.conf.get_file_path('config','delete_data_key_conf.yml'))

    def sql_delete_data(self):
        '''
        利用sql删除已创建的订单
        :return:
        '''
        database_conf_dict = self.database_dict.get('ysxd').get(self.environment_name)  #配置文件中对应环境数据库参数
        host = database_conf_dict.get('host')
        port = database_conf_dict.get('port')
        database = database_conf_dict.get('database')
        user = database_conf_dict.get('user')
        password = database_conf_dict.get('password')
        postgresql = OperarePostgresql(host=host,port=port,database=database,user=user,password=password)
        try:
            postgresql.execute("DELETE from attachment where shipment_demand_id in (%s);"%self.get_create_order_id())
            postgresql.execute("DELETE from reference_order where shipment_demand_id in (%s);" % self.get_create_order_id())
            postgresql.execute("DELETE from cargo_info_line where shipment_demand_id in (%s);" % self.get_create_order_id())
            postgresql.execute("DELETE from container_info where shipment_demand_id in (%s);" % self.get_create_order_id())
            postgresql.execute("DELETE from vehicle_info where shipment_demand_id in (%s);" % self.get_create_order_id())
            postgresql.execute("DELETE FROM shipment_participant_entity where shipment_demand_id in (%s);" % self.get_create_order_id())
            postgresql.execute("DELETE from message_record where shipment_demand_id in (%s);" % self.get_create_order_id())
            postgresql.execute("DELETE from shipment_demand where id in (%s);" % self.get_create_order_id())
            postgresql.commit()
            self.log.info('删除订单id：(%s)成功'%self.get_create_order_id())
        except Exception as e:
            excepttion = str(traceback.format_exc())
            self.log.error('删除失败：\n%s'%excepttion)

    def get_create_order_id(self):
        '''
        获取已创建订单的id
        :return: 将订单id列表以字符串返回
        '''
        order_id_list = []
        delete_data_key_list = self.delete_data_key_dict.get('shipment_demand_key')     #获取配置文件的delete_data_key_conf.yml的key
        for key in delete_data_key_list:
            order_id = self.global_dict.get(key)
            if order_id:
                order_id_list.append(order_id)
        order_ids = (','.join(str(x) for x in order_id_list))
        return order_ids

    # def delete_middle_data(self):
    #     'delete   from contact_partner_address where contact_partner_id in '
    #     'delete  from contact_partner where contact_partner_id in '

    def get_create_middle_data(self):
        '''
        获取收发货方及收发货地址id
        :return: 以字典返回
        '''
        contacts_key_list = self.delete_data_key_dict.get('middle_data_key').get('contacts_key') #收发货方key
        contacts_id_list = []
        for key in contacts_key_list:
            contacts_id = self.global_dict.get(key)
            if contacts_id:
                contacts_id_list.append(contacts_id)

        contacts_addr_key_list = self.delete_data_key_dict.get('middle_data_key').get('contacts_addr_key') #收发货地址key
        contacts_addr_id_list = []
        for key in contacts_addr_key_list:
            contacts_addr_id = self.global_dict.get(key)
            if contacts_addr_id:
                contacts_addr_id_list.append(contacts_addr_id)
        middle_test_data = {}
        middle_test_data['contacts_ids'] = contacts_id_list
        middle_test_data['contacts_addr_ids'] = contacts_addr_id_list
        return middle_test_data


if __name__ == '__main__':
    d = DeleteTestData({"cn_rail_order_id":4558959771548823552,"shpper_id":978451341,"shpper_addr_id":789413456})
    # print(d.sql_delete_data())
    print(d.get_create_middle_data())