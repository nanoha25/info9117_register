import unittest
from Python import enterPassword
from Python import enterUsername

class NormalUserRegisterTestCase(unittest.TestCase):

    def setUp(self):
        '''set up part'''
        #self.username = ("testname")
        #self.password = ("testpassword")
        #self.email = ("test@test.com")
        pass

    def test_enterUserName(self):
        self.assertEqual(self, "testname")

    def test_enterPassword(self):
        self.assertEqual(self, "testpassword")

    def test_enterEmail(self):
        self.assertEqual(self, "test@test.com")

    def tearDown(self):
        '''tear down part'''
        pass

if __name__ == '__main__':
    unittest.main()