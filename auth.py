class Credentials:
    '''
    class that generates new credentials intsances
    '''
    credentials_list = [] #Empty credentials list
    def __init__(self , account_name , password):
        '''
        init method to create instances of the credentials class
        '''
        self.account_name = account_name
        self.password = password