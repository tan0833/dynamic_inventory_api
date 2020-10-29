import unittest

class Test001(unittest.TestCase):

    a = '''
            try:
                self.assertEqual(1, 2)
            except AssertionError as e:
                self.assertEqual(1, 1)
            '''

    def test_aa(self):
        exec(self.a)


if __name__ == '__main__':
    # unittest.main()
    a = {"aa":{"bb":{"cc":13}}}
    dict = {'Name': 'Zara', 'Age': 7,"aa":{"bb":{"cc":12,"dd":1}}}
    dict2 = {'Sex': 'female'}
    # dict['aa']['bb']['cc'] = 5
    exec("dict['aa']['bb']['cc']='mm'")


    # print(dict)


