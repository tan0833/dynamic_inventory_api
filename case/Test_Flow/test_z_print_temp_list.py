from config.global_dict import temp_list
from config.Log import Log
import unittest


class TestTempList(unittest.TestCase):

    def test_z_temp_list(self):
        log = Log()
        log.warning('创建订单数量：%d'%len(temp_list))

        log.warning(temp_list)

if __name__ == '__main__':
    unittest.main()
