import random  
from user import User, Info
# import pyperclip

def register_user(username, password):
    '''
    creating a function to create users to the application
    '''
    new_user = User(username, password)
    return new_user

def save_user(user):
    '''
    Created a user function to save the new user
    '''
    User.register(user)

def check_user(username, password):
    '''
    function for verifying  user
    '''
    checking_user = Info.check_User(username, password)
    return checking_user

def create_info(username_name, account_name, info_details, password):
    '''
    function to create new information of a user
    '''
    new_info = Info(username_name,account_name, info_details, password)
    return new_info
    
def save_info(info):
    '''
    function to save new info inputed by the user
    '''
    Info.save_info(info)

def clipboard_info():
    '''
    function that copies my info to the clipboard
    '''
    return Info.clipboard_info(info_details)

def main():
    while True:
     

        print("▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌")
        print("▐░█▀▀▀▀▀▀▀▀▀ ▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀█░▌ ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ")
        print("▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌     ▐░▌          ")
        print("▐░▌          ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌     ▐░▌     ▐░█▄▄▄▄▄▄▄▄▄ ")
        print("▐░▌          ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░▌     ▐░░░░░░░░░░░▌")
        print("▐░▌          ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀█░█▀▀      ▐░▌      ▀▀▀▀▀▀▀▀▀█░▌")
        print("▐░▌          ▐░▌       ▐░▌▐░▌     ▐░▌       ▐░▌               ▐░▌")
        print("▐░█▄▄▄▄▄▄▄▄▄ ▐░▌       ▐░▌▐░▌      ▐░▌  ▄▄▄▄█░█▄▄▄▄  ▄▄▄▄▄▄▄▄▄█░▌")
        print("▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌")
        print(" ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀ ")
    
        print("\n")
        print("**"*50)
        print("******Welcome to password locker******")
        print("\n")
        print("Choose one option below \n 1. Create account \n 2. sign in \n 3. quit \n")

        choice = input("Enter choice : \n")
        if choice == "3":
            break

        elif choice == "1":
            print("**"*50)
            print("Create a new account")
            print ("\n")
            username = input('Create a username  ')
            password= input("Create password  ")
            save_user(register_user( username, password))
            print("Account created successfully!!")

        elif choice == "2":
            print("**"*50)
            print("Log in by entering your account credentials")
            username = input("Enter your username : \n")
            password = input("Enter your password : \n")
            user_exists = Info.check_User(self,userusername,password)
           
            if user_exists == username :
                print ("\n")
                print("Welcome to password Locker")

                
                                        
               
                while True:
                    print("\n")
                    print("**"*50)
                    print("Choose an option")
                    print("1. Create login information \n 2. copy login infomation \n 3. Exit ")
                    user_Choice = input("Enter choice : ")
                   
                if user_Choice == "3":
                    print('Goodbye {username}')
                    break
                    
                elif user_Choice == "1":
                    print("\n")
                    print("Enter your infomation")
                    account_name = input("Enter account name : \n")
                    info_details = input("Enter the site name : \n")
                    password = input("Enter password for site: \n")
                    save_info(create_info(username,account_name,info_details, password))
                    print("\n")
                    print("Credentials created successfully.")
                    
                elif user_Choice == "2":
                    print("\n")
                    print("**"*50)
                    choosen_info = input("Enter the site account to copy your info from. \n")
                    copy_info(choosen_info)
                    print("Successfully copied!")
                    print("\n")
                    
                else:
                    print("Enter correct option and try again!!!")
                                    

            else:
                print("Wrong info entered")
        else:
            print("wrong info entered")

if __name__ == '__main__':
   main()