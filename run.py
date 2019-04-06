#!/usr/bin/env python3.6
import getpass
from user import User

def create_user(first_name , last_name):
    '''
    Function to create new user
    '''
    new_user = User(first_name , last_name)
    return new_user

def save_users(user):
    '''
    function to save user
    '''
    user.save_user()

def check_existing_users(first_name , last_name):
    '''
    function to check user exists
    '''
    return User.user_exist(first_name , last_name)

def main():
    print("********************Welcome to password locker********************")
    # print('\n')
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
    print("*******Choose an option******")
    print('would you like to proceed? (y/n)')
    first_choice = input().lower()
    if first_choice == 'y':
        print('[1 = Agree].Sign-up')
        log_sign = input()
        if log_sign == '1':
            print('First name')
            f_name = input().lower()
            print("Last name ")
            l_name = input().lower()
            print('password')
            pswd_a = getpass.getpass('Password:')
            print('Confirm password')
            pswd_b = getpass.getpass('Password:')
            save_users(create_user(f_name,l_name)) 
            if pswd_a == pswd_b:
                print(f"New user {f_name} {l_name} created")
            else:
                print('Passwords don\'t match')
            print('Enter your first name to log in')
            name = input().lower()
            print('Enter your password')
            pswd_c = getpass.getpass('Password:')
            if pswd_c == pswd_a and f_name == name:
                print(f'Logged in as {f_name}')
            else:
                print('user name or password incorrect')
            print(' View existing acconts')
            print('Add new account')                             
            acnt = input()
            if acnt == '2':
                print('Account name')
                acnt_name = input()
                print('Password')
                acnt_passA = getpass.getpass('Password:')
                print('Confirm password')
                acnt_passB = getpass.getpass('Password:')
                if acnt_passA == acnt_passB:
                    print(f'New {acnt_name} account created!')
                    print('[a=] Display Existing accounts                        [b=] Exit')
                    view_acnt = input()
                    while view_acnt == 'b':
                        break
                    if view_acnt == 'a':
                        print('Here are your accounts')   
    elif first_choice == 'n':
        print('Bye')

    else:
        print('Invalid choice, Choose between (y = yes) and (n = no)')
if __name__ == '__main__':

    main()
