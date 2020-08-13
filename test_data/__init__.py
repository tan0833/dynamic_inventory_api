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
    unittest.main()

