import pyperclip
class User:
    '''
    the user class
    '''
    user_list = []

    def __init__(self, first_name, last_name, number, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = number
        self.email = email
        self.password = password

    def save_user(self):
        '''
        this saves the user into the user_list
        '''
        User.user_list.append(self)

    def delete_user(self):
        '''
        this deletes the user saved from the user_list
        '''
        User.user_list.remove(self)

    @classmethod
    def find_by_first_name(cls, first_name):
        '''
        finds the first name and displays it
        '''
        for user in cls.user_list:
            if user.first_name == first_name:
                return user        
    
    @classmethod
    def user_exist(cls, first_name):
        '''
        confirms whether the user does exist or not
        '''
        for user in cls.user_list:
            if user.first_name == first_name:
                return True
        else:
            return False

     @classmethod
    def display_users(cls):
        '''
        display the contact list by returning it
        '''
        return cls.user_list

