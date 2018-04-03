import unittest # Importing the unittest mode
from user import User # Importing the User Class
import pyperclip

class TestUser(unittest.TestCase):
    """
    Test class that defines the test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    """

    def setUp(self):
        """
        Set up method to run before each test cases.
        """
        self.new_user =User(
            "Kim","Possible","ihaveaboyfriend") # create user object

    def tearDown(self):
        """
        tearDown method that does clean up after each test case has run
        """
        User.user_list = []

    def test_init(self):#test_init, test_instance
        """
        test_init test case to test if the object is initialized properly
        """

        self.assertEqual(self.new_user.first_name, "Kim")
        self.assertEqual(self.new_user.last_name, "Possible")
        self.assertEqual(self.new_user.password, "ihaveaboyfriend")

    def test_save_user(self):
        """
        test_save_user test case to test if the user object is saved into the user_list
        """
        self.new_user.save_user() #saving the new user
        self.assertEqual(len(User.user_list),1)

    def test_save_multiple_user(self):
        """
        test_save_multiple_user to check if we can save multiple users
        objects to our user_list
        """
        self.new_user.save_user()
        test_user = User(
             "Ron", "Stopabble", "ilovekim") # new User
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

    def test_delete_user(self):
        """
        test_delete_user to test if we can remove a user from our user_list
        """
        self.new_user.save_user()
        test_user = User(
             "Ron", "Stopabble", "ilovekim") # new User
        test_user.save_user()

        self.new_user.delete_user()# Deleting a user object
        self.assertEqual(len(User.user_list),1)


    def test_find_user_by_first_name(self):
        """
        test to check if we can find a user by account_name and display information
        """

        self.new_user.save_user()
        test_user = User(
             "Ron", "Stopabble", "ilovekim") # new User
        test_user.save_user()

        found_user = User.find_by_number("Ron")

        self.assertEqual(found_user.password, test_user.password)

    def test_user_exists(self):
        """
        test to check if we can return a Boolean if we cannot find the user.
        """

        self.new_user.save_user()
        test_user = User(
             "Ron", "Stopabble", "ilovekim") # new User
        test_user.save_user()

        user_exists = User.user_exist("Ron")

        self.assertTrue(user_exists)

    def test_display_all_users(self):
        """
        method that returns a list of all users saved
        """

        self.assertEqual(User.display_users(),User.user_list)

    def test_copy_password(self):
        """
        Test to confirm that we are copying the password from a found user
        """

        self.new_user.save_user()
        User.copy_password("Kim")

        self.assertEqual(self.new_user.password,pyperclip.paste())

if __name__ == '__main__':
    unittest.main()
