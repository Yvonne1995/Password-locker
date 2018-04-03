from passw import Passwords
import pyperclip
import unittest

class TestPasswords(unittest.TestCase):

    """
    Test class that defines the test cases for the passwords class behaviors.

    Args:
        unitest.TestCase: TestCase class that helps in creating test cases

    """

    def setUp(self):
        """
        setUp method to run before each test cases.
        """

        self.new_profile = Passwords(
            "KoolKid", "ilovemyboyfriend", "16")

    def tearDown(self):
        """
        tearDown method that does clean up after each test case has run
        """
        Passwords.password_list = []

    def test_init(self):
        """
        test_init test case to test if the object is initialized properly
        """

        self.assertEqual(self.new_profile.account_name, "KoolKid")
        self.assertEqual(self.new_profile.account_password,
                         "ilovemyboyfriend")
        self.assertEqual(self.new_profile.password_length,
                         "16")

    def test_save_profile(self):
        """
        test_save_contact test case to test if the password object is saved into
            the password_list
        """
        self.new_profile.save_profile()
        self.assertEqual(len(Passwords.password_list), 1)

    def test_save_multiple_profiles(self):
        """
        test_save_multiple_profiles to check if we can save multiple profile objects to our contact_list
        """
        test_profile = Passwords("Gmail", "ilovemygirlfriend", "17")
        """
        test_profile does not need "self". Its a local variable
        """
        test_profile.save_profile()
        self.new_profile.save_profile()
        self.assertEqual(len(Passwords.password_list), 2)

    def test_find_by_account(self):
        """
        Test to check if we can find our passwords by account and display.
        """
        test_profile = Passwords("Gmail", "ilovemygirlfriend", "17")
        test_profile.save_profile()

        found_profile = Passwords.find_by_account("Gmail")

        self.new_profile.save_profile()
        self.assertEqual(found_profile.account_password,
                         test_profile.account_password)

    def test_profile_exists(self):
        """
        Test to check if we can return a boolean if we cannot find a profile
        """

        self.new_profile.save_profile()
        test_profile = Passwords("Gmail", "ilovemygirlfriend", "17")
        test_profile.save_profile()

        test_exists = Passwords.profile_exists("Gmail")
        self.assertTrue(test_exists)

    def test_display_profiles(self):
        """
        Method that displays the list of all the profiles saved
        """
        self.assertEqual(Passwords.display_profiles(), Passwords.password_list)

    def test_copy_password(self):
        """
        Method that confirms we are copying the password from a profile
        """
        self.new_profile.save_profile()
        Passwords.copy_password("KoolKid")

        self.assertEqual(self.new_profile.account_password, pyperclip.paste())

    def test_password_gen(self):
        """
        We want to test if our password generator will work.
        """
        self.new_profile.save_profile()
        random_password = self.new_profile.password_gen("17")
        self.assertNotEqual(random_password, self.new_profile.account_password)


if __name__ == "__main__":
    unittest.main()
