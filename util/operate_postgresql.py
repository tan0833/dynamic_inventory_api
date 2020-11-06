'''postgresql的相关操作'''

import psycopg2


class OperarePostgresql:

    def __init__(self,user,password,database,host,port=5432):
        '''

        :param user: 用户名
        :param password: 密码
        :param database: 数据库名称
        :param host: 连接地址
        :param port:端口
        '''
        self.conn = psycopg2.connect(database=database, user=user,password=password, host=host, port=port)
        self.cursor = self.conn.cursor()


    def execute(self,*args):
        '''
        执行sql
        :param args:
        :return:
        '''
        self.cursor.execute(*args)

    def commit(self):
        '''
        提交
        :return:
        '''
        self.conn.commit()

    def fetchall(self):
        '''
        获取全部数据
        :return:
        '''
        return self.cursor.fetchall()

    def fetchone(self):
        '''
        获取一条数据
        :return:
        '''
        return self.cursor.fetchone()

    def close(self):
        '''
        关闭
        :return:
        '''
        self.cursor.close()
        self.conn.close()

if __name__ == '__main__':
    pg = OperarePostgresql(database='shipment_demand',host='10.25.7.107',user='postgres',password='123',port=5432)

    aa ='''INSERT INTO public.shipment_demand (id, created_by, created_time, last_modified_by, last_modified_time, org_id, proxy_operator, bulk_carton_qty, bulk_carton_qty_unit_code, cargo_description, cargo_type_code, gross_weight, gross_weight_unit_code, piece_qty, piece_qty_unit_code, total_package_qty, total_package_qty_unit_code, total_volume, total_volume_unit_code, deleted, deleted_by, deleted_time, demand_status_code, multi_tenancy_code, multi_tenancy_name, request_account_id, request_account_mail, request_account_name, request_account_tel, send_status, cost_code, settlement_company_name, settlement_crm_code, settlement_legal_person, settlement_party_id, shipment_order_no, designated_airport, discharge_airport_id, origin_airport_id, consignee, consignee_id, destination_city_id, incoterms_code, loading_type_code, logistic_type_code, origin_city_id, payment_type_code, designated_railway_station, discharge_railway_station_id, origin_railway_station_id, receiving_address_abbreviation, receiving_address_code, receiving_address_detail, receiving_city_code, receiving_city_name, receiving_contact_name, receiving_address_id, receiving_country_code, receiving_country_name, receiving_district_code, receiving_district_name, receiving_email, receiving_mobile_number, receiving_post_code, receiving_province_code, receiving_province_name, receiving_street_code, receiving_street_name, receiving_telephone_number, receiving_mobile_area, receiving_telephone_area, required_arrival_time, required_pickup_time, designated_seaport, discharge_seaport_id, origin_seaport_id, service_mode_code, shipper, shipper_id, shipping_address_abbreviation, shipping_address_code, shipping_address_detail, shipping_city_code, shipping_city_name, shipping_contact_name, shipping_address_id, shipping_country_code, shipping_country_name, shipping_district_code, shipping_district_name, shipping_email, shipping_mobile_number, shipping_post_code, shipping_province_code, shipping_province_name, shipping_street_code, shipping_street_name, shipping_telephone_number, shipping_mobile_area, shipping_telephone_area, uturn, uturn_area_code, uturn_document_code, vehicle_require, shipping_mode_code, status_call_back_info, transnational_shipment, cargo_value, currency_code, escort_type_code, insurance, insured_value, need_container_jit, need_discharge, need_escort, need_load, pod, speedway, urgent, version, bill_of_lading_type_code, entrust_customs_declaration, entrusted_party, entrusted_party_id, eta, etd, partial_shipment_allowed, remarks, self_provided_cabinet, transhipment_allowed, request_account_company_crm_code, shipper_name, consignee_name, entrusted_party_name, shipment_no, master_bill_no, shipping_address_partner_id, receiving_address_partner_id, origin_location_code, destination_location_code, shipping_location_code, receiving_location_code, shipping_address_same_as_shipper, receiving_address_same_as_consignee, is_shipper_default_shipping_address, is_consignee_default_receiving_address, house_bill_no, source_system_code, source_system_order_no, letter_of_attorney_export_task_id, letter_of_attorney_oss_id, letter_of_attorney_generate, error_messages, marks_and_numbers, request_account_company_country_code, follow, customs_broker, return_demand, forward_demand_id, forward_shipment_order_no) VALUES (4558959771548823552, '4491649430630440960', '2020-11-04 07:23:13.282569', '4491649430630440960', '2020-11-04 07:23:13.282569', 'ORG10046', null, null, null, null, null, null, null, null, null, null, null, null, null, false, null, null, 0, 'CP_MANAGER', '平台虚拟租户', '4491649430630440960', 'admin26@123.com', 'admin26', '+86-9527', 0, null, null, null, null, null, null, null, null, null, '{"contactPartnerId":4443901033658114048,"contactPartnerName":"111颂1111","contactPartnerType":"CONSIGNEE","tenantCode":null,"deletedFlag":null,"companyId":null,"addressAbbreviation":"怎么办AC","addressCode":"1211","countryCode":"CN","countryName":"CHINA","provinceCode":"CN-45","provinceName":"GUANGXI ZHUANG AUTONOMOUS REGION","cityCode":"SCI105678","cityName":"HECHI","districtCode":"","districtName":null,"streetCode":null,"streetName":null,"addressDetail":"111","transportLocationCode":"CNHCH","postCode":"1111","contactName":"111","telephoneNumber":"2131111","telephoneArea":"93","mobileNumber":"43878","mobileArea":"123123","email":null}', 4443901033658114048, null, null, null, null, 'SCI105621', 'PYT_PB3', null, null, null, '怎么办AC', '1211', '111', 'SCI105678', 'HECHI', '111', 4501149211095048192, 'CN', 'CHINA', '', null, null, '43878', '1111', 'CN-45', 'GUANGXI ZHUANG AUTONOMOUS REGION', null, null, '2131111', '123123', '93', '2020-11-06 07:23:00.152000', '2020-11-04 08:22:00.658000', null, null, null, 'SEL_F2D', '{"contactPartnerId":4443194691926548480,"contactPartnerName":"123123213","contactPartnerType":"SHIPPER","tenantCode":null,"deletedFlag":null,"companyId":null,"addressAbbreviation":"1111","addressCode":null,"countryCode":"CN","countryName":"CHINA","provinceCode":"CN-35","provinceName":"FUJIAN PROVINCE","cityCode":"SCI105561","cityName":"PUTIAN","districtCode":"","districtName":null,"streetCode":null,"streetName":null,"addressDetail":"112211221","transportLocationCode":"CNPUT","postCode":"1221121111111111111111111","contactName":"121212111111","telephoneNumber":"355111","telephoneArea":"1264","mobileNumber":"13213213","mobileArea":"0086","email":"dfasdf@11.com"}', 4443194691926548480, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, 'TPM_EXPRESS', null, false, null, null, null, null, null, null, null, null, null, null, null, null, 0, null, null, null, null, null, null, null, null, null, null, null, '123123213', '111颂1111', null, null, null, null, 4443901033658114048, null, null, null, 'CNHCH', null, true, null, true, null, 'JUSLINK_SHIPMENT_DEMAND', null, null, null, null, null, null, 'VI', false, null, false, null, null);'''

    pg.execute(aa)

    bb = """DELETE from shipment_demand where id in ('4558959771548823552');"""
    pg.execute(bb)
    pg.commit()