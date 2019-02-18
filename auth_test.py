import unittest
from auth import Credentials

class TestCredentials(unittest.TestCase):
    '''
    testcase class to define the test case behaviour of the credentials class 
    Args:
        unittest.TestCredentials: TestCredentials class that helps in creating test cases
    '''

    def setUp(self):
        '''
        setUp test to run before each test case of the TestCredentials class
        '''
        self.new_credentials = credentials('snapchat' , 'Chris')

    def tearDown(self):
        '''tear down method to clean up after every test of the credentials class
        '''
        Credentials.credentials_list = [] #Returns an empty credentials list after every test


    def test_init_credentials(self):
        '''
        Test to see if accounts are instanciated properties
        '''
        self.assertEqual(self.new_credentials.account_name , 'Instagram')
        self.assertEqual(self.new_user.password , 'Chris')