import unittest


class FirstStringTest(unittest.TestCase):

    # Return true or false.
    def test_StringUpper(self):
        self.assertEqual('foo'.upper(), 'FOO', 'Something wrong')


if __name__ == '__main__':
    unittest.main()