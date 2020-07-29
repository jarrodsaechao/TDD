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

    def test3(self):
        input = "aquafina"
        expected = True
        self.assertEqual(check_pwd(input), expected)

    def test4(self):
        input = "AQUAFINA"
        expected = True
        self.assertEqual(check_pwd(input), expected)

    def test5(self):
        input = "Aquafina"
        expected = True
        self.assertEqual(check_pwd(input), expected)

    def test6(self):
        input = "AquafinaH20"
        expected = True
        self.assertEqual(check_pwd(input), expected)

    def test7(self):
        input = "AquafinaH20  "
        expected = True
        self.assertEqual(check_pwd(input), expected)

    def test8(self):
        input = "AquafinaH20!"
        expected = True
        self.assertEqual(check_pwd(input), expected)

if __name__ == '__main__':
    unittest.main()