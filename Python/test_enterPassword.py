import unittest
from Python import enterPassword

class EnterUsernameTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def test_valid_password(self):
        self.assertEqual(enterPassword, "pswdtest1")
        return "Successful."

    def test_empty_password(self):
        self.assertEqual(enterPassword, "")
        return "Invalid password"

    def test_numeric_password(self):
        self.assertEqual(enterPassword, "123456789")
        return "Weak password"

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()