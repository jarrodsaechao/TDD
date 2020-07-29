import unittest
from check_pwd import check_pwd

class TestCase(unittest.TestCase):

    def test1(self):
        input = "this is right"
        expected = True
        self.assertEqual(check_pwd(input), expected)

    def test2(self):
        input = "Church"
        expected = True
        self.assertEqual(check_pwd(input), expected)

if __name__ == '__main__':
    unittest.main()