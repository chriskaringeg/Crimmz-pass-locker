
import random
import string

global user_list
class User:
    """
    Class that generates new instances of the user to sign up.
    """
    info_list = [] #empty info list
    user_list = [] #Empty user list
    #this are instance variables
    def __init__(self,username,password):
        self.username = username
        self.password = password

    def register(self):
       User.user_list.append(self)

class Info:
    '''
    Class to create new infomation of a user
    '''
    info_list = []
    users_info = []

    def __init__(self, username_name, account_name, info_details, password):
        self.username_name = username_name
        self.account_name = account_name
        self.info_details = info_details
        self.password = password

    def save_info(self):
        '''
        created a function to new info of a user
        '''
        Info.info_list.append(self)

    
    @classmethod
    def clipboard_info(cls, info_details):
        '''
        method that copies the user info to the clipboard
        '''
        find_info = Info.find_by_info_details(info_details)
        # return pyperclip.copy(find_info.password)


    @classmethod
    def check_User( username, password):
        '''
        method for checking user if exists in the user list array
        '''
        super_user = ""
        for user in User.user_list:
            if (user.username == username and user.password == password):
                super_user = user.username
            return super_user
        

    @classmethod
    def find_by_site_name(cls, info_details):
        '''
        method that takes in a site name and gives out info matching site name
        '''
        for information in cls.info_list:
            if information.info_details == info_details:
                return information
    
   