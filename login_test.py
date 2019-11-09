import unittest
import pyperclip
from user import User  # user class import
class TestUser(unittest.TestCase):
    '''
    defines test case for user
    '''
# test 1 : to check if it's been istantiated correctly
    def setUp(self):
        self.new_user = User("Test", "user", "0798765431", "testuser@mail.com", "password")  # user object
    def test_init(self):
        self.assertEqual(self.new_user.first_name, "Test")
        self.assertEqual(self.new_user.last_name, "user")
        self.assertEqual(self.new_user.phone_number, "0798765431")
        self.assertEqual(self.new_user.email, "testuser@mail.com")
        self.assertEqual(self.new_user.password, "password")

# test 2 : test for saving
    def test_save_user(self):
        '''
        test if a new user can be saved
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)

# test 3 : for saving multiple users
    def tearDown(self):
        '''
        gets cleared after each test runned
        '''
        User.user_list = []
    def test_save_multiple_user(self):
        '''
        test if multiple users can be saved
        '''
        self.new_user.save_user()
        test_user = User("Test", "user", "0798765431","testuser@mail.com", "password")
        test_user.save_user()
        self.assertEqual(len(User.user_list), 2)

# test 4 : for deleting
    def test_delete_user(self):
        '''
        deletes a user
        '''
        self.new_user.save_user()
        test_user = User("Test", "user", "0798765431", "testuser@mail.com", "password")
        test_user.save_user()
        self.new_user.delete_user()
        self.assertEqual(len(User.user_list), 1)

# test 5 : find user by first name
    def test_find_user_by_first_name(self):
        '''
        finds the user's first name and displays it
        '''
        self.new_user.save_user()
        test_user = User("Test", "user", "0798765431", "testuser@mail.com", "password")
        test_user.save_user()
        self.new_user.delete_user()
        self.assertEqual(len(User.user_list), 1) 

# test 6 : if a user exists
    def test_user_exists(self):
        '''
        returns a true or false if a user does or doesn't exists
        '''
        self.new_user.save_user()
        test_user = User("Test", "user", "0798765431", "testuser@mail.com", "password")
        test_user.save_user()
        user_exists = User.user_exist("Test")
        self.assertTrue(user_exists)


# test 7 : display all contacts
    def test_display_all_users(self):
        '''
        displays all contacts saved in the list
        '''
        self.assertEqual(User.display_users(), User.user_list)


