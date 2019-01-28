import unittest
import pyperclip
from user import User, Info
from password import register_user

class TestUser (unittest.TestCase):
    '''
	Test class that defines test cases for the user class behaviours.
	Args:
	    unittest.TestCase: helps in creating test cases
	'''
    # def setUp(self):
	#     '''
    #     Function to create a user account before each test
    #     '''
    # self.new_user = User("Clinton","admin")

    def test__init(self):
        '''
		Test to if check the initialization/creation of user instances is properly done
		'''
    self.assertEqual(self.new_user.username,'Clinton')
    self.assertEqual(self.new_user.password,'admin')

    def test_save_user(self):
        '''
		Test to check if the new users info is saved into the user list
	    '''
    self.new_user.register()
    self.assertEqual(len(User.user_list),1)

if __name__ == '__main__':
	unittest.main()
