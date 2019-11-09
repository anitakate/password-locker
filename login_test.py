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