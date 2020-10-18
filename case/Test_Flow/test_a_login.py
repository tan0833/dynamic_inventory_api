import unittest
from api_pack.api_business.login import Login
from config.global_dict import temp_dict

class TestLogin(unittest.TestCase):

    def test_login(self):
        login = Login()
        token = login.login_business('HP02','Jusda#123')
        temp_dict['token'] = token