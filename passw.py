# BDD
# 1. Open account
# 2. Generate password
# 3. Save password
# 4. Tear down
# 5. Save multiple
# 6. Delete password profile
# 7. Find by profile
# 8. Copy paste

import random
import pyperclip
import string

class User:
    def __init__(self, first_name, last_name, profile_key):
        self.first_name = first_name
        self.last_name = last_name
        self.profile_key = profile_key

class Passwords:
    """
    Class that generates and records new instances of passwords for User.
    """
    password_list = []

    def __init__(self, account_name, account_password, password_length):
        self.account_name = account_name
        self.account_password = account_password
        self.password_length = password_length

    def save_profile(self):
        """
        save_profile method saves password objects int password_list
        """
        Passwords.password_list.append(self)

    @classmethod
    def profile_exists(cls, account_name):
        """
        Method that checks if a profile exists from the password_list.
        Arg:
            account_name: Account name to search if it exists
        Returns:
            Boolean: True or false depending if the profile exists
        """
        for profile in cls.password_list:
            if profile.account_name == account_name:
                return True
            return False

    @classmethod
    def display_profiles(cls):
        """
        method that returns profile list
        """
        return cls.password_list

    @classmethod
    def find_by_account(cls,account_name):
        """
        Method that takes in account_name and returns password matching the account.

        Args:
            number: account_name to search for
        Returns:
            Password matching the account_name.
        """
        for profile in cls.password_list:
            if profile.account_name == account_name:
                return profile

    @classmethod
    def copy_password(cls, account_name):
        password_found = Password.find_by_account(account_name)
        pyperclip.copy(password_found.account_password)

    # @classmethod
    # def password_gen ():
    # from random import *
    # characters = string.ascii_letters+string.punctuation+string.digits
    # password = "".join(choice(characters) for x in range(randint(8,16)))
    # print(password)


    @classmethod
    def password_gen(cls, password_length):
        string = "abcdefghigjkmnopqrstuvwxyz1234567890-_=+{}\|"';>./,`!@#$^&*()`'
        password = "".join(random.sample(string, int(password_length)))
        account_passsword = password
        return account_passsword



# import string,random
#
# def generatePassword(num):
#     password = ''
#
#     for n in range(num):
#         x = random.randint(0,94)
#         password += string.printable[x]
#
#     return password
#
# print generatePassword(16)

# import string
# from random import *
# characters = string.ascii_letters+string.punctuation+string.digits
# password = "".join(choice(characters) for x in range(randint(8,16)))
# print(password)
