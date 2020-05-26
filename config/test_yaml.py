# import yaml
# import json
from config.get_conf import Conf
#
# p = Conf().get_file_path('data','test.yml')
#
# result = yaml.load(open('test.yml'))
#
# print(json.dumps(result))

import requests

url = "https://j1.sccpcloud.com/api-gateway/oss/objects"

payload = {'fileName': 'shiyong1',
'bucketDirs': 'ShipmentDemand'}
file_path = Conf().get_file_path('runMain','__init__.py')
files = [
  ('file', open(file_path,'rb'))
]

headers = {
  'Authorization': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0ZXJtaW5hbF90eXBlIjoid2ViIiwidXNlcl9uYW1lIjoiSFAiLCJzY29wZSI6WyJyZWFkIiwid3JpdGUiLCJmb28iXSwiYXBwbGljYXRpb25fY29kZSI6ImhvbWUiLCJleHAiOjE1OTA1MTA0NDcsInVzZXJhY2NvdW50X2lkIjoiNDQyODM2MTM1MjM1MzY3MzIxNiIsImp0aSI6ImY2OTVjMTcwLTk2YWUtNDhhNS1iYzg0LTM2NmE1Nzk3ODczMyIsImNsaWVudF9pZCI6ImhvbWUifQ.OOZQddoB99MF_8plUxSzcvgf3lwOhKS3WKUssDZe1W5FHRF0JBfhv7HoMO5dIJOMJCbkW1ZQ81Cl2cxB4_-nqOhlgNlBRvGD0yKb4Q-NZMemgDGKL3TLt5rjQyhI0vxuUMJh286YLydIFHgffEw3wjj2ZL7VUDvTE-TtCzwFo9xlrEOOpb4WypYi7Tbb_p_Vipgzhe3kF7oUjGQ46c_SqsMN6X5c2M97ElrPO3Irng1r94uW-0Q0pRqeme7MqzkU7hFhzcFOFh_LkBeI9UOOvphaJrcSJ6uhx560NsfKJJRjzNWbm-qvUFeg76BLAs_dN7YxlNqCXYcyJfaSRy8iuw',
  'clientId': 'client'
}

response = requests.request("POST", url, headers=headers, data = payload, files = files)

print(response.text.encode('utf8'))
