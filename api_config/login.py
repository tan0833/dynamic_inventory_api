from config.get_conf import Conf
import unittest

class Login(unittest.TestCase):

    def test_login(self):
        b = Conf().get_file_path('api_config','login_api.yml')
        a = Conf().get_yaml(b)
        print(a)




if __name__ == '__main__':
    # l = Login()
    unittest.main()