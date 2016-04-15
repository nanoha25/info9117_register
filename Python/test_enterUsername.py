import unittest
from Python import enterUsername

class EnterUsernameTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def test_valid_name(self):
        self.assertEqual(enterUsername, "testnanoha")
        return "Successful."

    def test_empty_name(self):
        self.assertEqual(enterUsername, "")
        return "No name."

    def test_invalid_name(self):
        self.assertEqual(enterUsername, "u$ern@me")
        return "Invalid name."

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()