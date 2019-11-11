#!/usr/bin/env python3.6

from user import User

def create_user(fname, lname, phone, email, password):
    '''
    creates new user
    '''
    new_user = User(fname, lname, phone, email, password)
    return new_user


def save_users(user):
    '''
    saves a new user
    '''
    user.save_user()


def del_user(user):
    '''
    deletes a user 
    '''
    user.delete_user()

def find_user(first_name):
    '''
    finds the user first name
    '''
    return User.find_by_first_name(first_name)

def check_existing_users(first_name):
    '''
    return a true or false whether the user exist or not
    '''
    return User.user_exist(first_name)

def display_users():
    '''
    function for displaying the users
    '''
    return User.display_users()
def generate_password(pass_len):
    '''
    generates the password
    '''
    return Credential.generate_password(pass_len)


def main():
    print("")
print("-"*20)
print(" Cate Spark Locker")
print("-"*20)
print("Sign Up to ")

print("Enter Username: ")
user_name = input()

print("Enter password: ")
user_password = input()

while True:
    print(f"{user_name}, what would you like to do?")
    print('\n')
    print("Use these short codes : cc - create a new credential, dc - display credentials, fc - find a credential, ex - exit the user list ")

    short_code = input().lower()

    if short_code == 'cc':
        print("New user")
        print("-"*8)
        print("-"*8)
        print("First name:-  ")

        f_name = input()
        print("Last name:-  ")

        l_name = input()
        print("Phone number:-  ")

        n_number = input()
        print("Email address:- ")

        e_address = input()
        print("Password:- ")

        p_password = input()
        print('\n')

        save_users(create_user(f_name,l_name,n_number,e_address,p_password))
        print('\n')
        print(f"New user {f_name} {l_name} created")
        print('\n')

    elif short_code == 'dc':
        if display_users():
            print("Here's a list a list of all users")
            print('\n')

            for user in display_users():
                print(f"User name:- {user.first_name} {user.last_name} \nPhone number:- {user.phone_number} \nEmail:- {user.email} \nPassword:- {user.password}")
                print('\n')
        else:
            print('\n')
            print("No credentials to display")
            print('\n')

    elif short_code == 'fc':
        print("Spark search")
        print("Enter first name: ")

        search_first_name = input()
        if check_existing_users(search_first_name):
            search_user = find_user(search_first_name)
            print(f"{search_user.first_name} {search_user.last_name} ")
            print('-' * 20)
            print(f"Phone number :- {search_user.phone_number}")
            print(f"Email address :- {search_user.email}")
            print(f"Password :- {search_user.password}")
        else:
            print("User does not exist!!")
    elif short_code == "ex":
        print(f"Bye, {user_name}. Have a lovely time.")
        break
    else:
        print("Hey Hey!! Invalid short code")

if __name__ == '__main__':

    main()
