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