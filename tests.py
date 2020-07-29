import unittest


class TestCase(unittest.TestCase):

    def test1(self):
        input = "this is right"
        expected = true
        self.assertEqual(fizz_buzz(input), expected)


if __name__ == '__main__':
    unittest.main()