import unittest
from user import User

class TestUser(unittest .TestCase):
    '''
    Tets case that defines test cases for the user class
    behaviours
    
    Args:
        unittest.TestUser: TestUser class that helps in creating test cases
    '''

    def setUp(self):
        '''
        set up method to run before each test cases
        '''
        self.new_user = User('Chris' , 'Karinge')

    def tearDown(self):
        '''tear down method to clean up after every test
        '''
        User.user_list = [] #Returns an empty user list after every test

    def test_init(self):
        '''
        Test to see if users are instanciated properties
        '''
        self.assertEqual(self.new_user.first_name , 'Chris')
        self.assertEqual(self.new_user.last_name , 'Karinge')


    def test_save_user(self):
        '''
        Test to see if users are saved in the user_list
        '''
        self.new_user.save_user() #saving new user
        self.assertEqual(len(User.user_list) , 1)


    def test_save_multiple_users(self):
        '''
        Test to see if multiple users can be saved
        '''
        self.new_user.save_user()
        dummy_user = User('Loise' , 'Kimani') #new dummy user
        dummy_user.save_user()
        self.assertEqual(len(User.user_list) , 2)


    def test_delete_user(self):
        '''
        Test to see if we can delete a user from user list
        '''
        self.new_user.save_user()
        dummy_user = User('Loise' , 'kimani')
        dummy_user.save_user()
        self.new_user.delete_user() #Deleting a user from the user list
        self.assertEqual(len(User.user_list) , 1)
  

    def test_display_all_users(self):
        '''
        method that returns a list of all users saved
        '''
        self.assertEqual(User.display_users() , User.user_list)
if __name__ == '__main__':
    unittest.main()
