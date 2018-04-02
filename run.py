#!/usr/bin/env python 3.6
from user import User
from passw import Passwords
import random

def create_user(fname, lname, password):
    """
    Function to create a new user_list
    """
    new_user =User(fname, lname, password)
    return new_user

def save_users(user):
    """
    Function to save user_list
    """
    user.save_user()

def del_user(user):
    """
    Function to delete a user
    """
    user.delete_user()

# def find_user(number):
#     """
#     Function that finds a user by number and returns the contract
#     """
#     return User.find_by_number(number)
#
# # Check if a contract exists
#
#
# def check_existing_user(number):
#     """
#     Function that checks if a user exists with that number and return Boolean
#     """
#     return User.user_exist(number)

def display_users():
    """
    Function that returns all the saved user_exist
    """
    return User.display_users()

def copy_password(number):
    """
    Function that copys to machine clipboard
    """
    return User.copy_password()

def create_profile(account_name, account_password, password_length):
    """
    Function to create new_profile
    """
    new_profile = Passwords(account_name, account_password, password_length)
    return new_profile

def save_profile(profile):
    """
    Function to save profile
    """
    profile.save_profile()

def find_profile(account_name):
    """
    Function that finds password by account_name and returns full details
    """
    return Passwords.find_by_account(account_name)

def check_existing_profile(account_name):
    """
    Function that check if a profile exists with that account_name and return a Boolean
    """
    return Passwords.check_existing_profile(account_name)

def display_profiles():
    """
    Function that returns all save profiles
    """
    return Passwords.display_profiles()

def copy_password(account_name):
    """
    Function that allows us to copy a password from matching
    account_name
    """
    return Passwords.copy_password()


def password_gen(password_length):
    return Passwords.password_gen(password_length)


def main():
    print("Hello! Welcome to your password manager. What is your name?")
    user_name = input()
    print("")

    print(f"Hi {user_name}. What would you like to do?")
    print("")

    while True:
        print("""Use these short codes:
               cn - create new account
               li - log in to your password profiles
               lo -log out of yur account
               ex - exit profile list. """)
        short_code = input().lower()
        print("_" * 100)
        if short_code == "cn":
            print("New Passwrd Locker Account")
            print("_" * 20)

            print("Enter first name -")
            f_name = input()

            print("Enter last name -")
            l_name = input()

            print("""
                 We can generate a password for you. Use:
                 g- to generate a password
                 m- to set your own.
                 """)
            pass_code = input().lower()
            print("__"*20)
            if pass_code == "g":
                password_length = int(
                    input("How long do you want your password - "))
                password = password_gen(password_length)
                print(f"Your new password is {password}")
            else:
                print("Write a password of your own. We'll store it for you")
                password = input()

            save_users(create_user(f_name, l_name, password))

            print("")
            print(
                f"""New account created for - {f_name} {l_name} your account password is - {password}""")
            print("")
            print("You can now create your password profiles")
        while True:
            print("""Use these short codes:
                  np - create password profile,
                  dp - display password locker profiles,
                  fp - find a password profile,
                  ex - exit profile list.""")
            short_code = input().lower()
            print("_" * 100)
            if short_code == "np":
                print(
                    "What account do you want to save a password for? Eg Gmail, Facebook, Equity")
                account_name = input()
                print("""
                      We can generate a password for you. Use:
                      g- to generate a password
                      m- to set your own.
                      """)
                pass_code = input().lower()
                print("__" * 20)
                if pass_code == "g":

                    password_length = int(
                        input("How long do you want your password - "))

                    password = password_gen(password_length)
                    print("")
                    print(f"Your password for {account_name} is: {password}")
                    print("")
                    print("__" * 20)
                else:
                    print("Write a password of your own. We'll store it for you")
                    password = input()
                    password_length = len(password)
                    print("")
                    print(f"Your password for {account_name} is: {password}")
                    print("")
                    print("__" * 20)

                save_profile(create_profile(
                    account_name, password, password_length))

            elif short_code == "dp":
                if display_profiles():
                    print("Here is a list of all you profiles")
                    print("")
                    for profile in display_profiles():
                        print(
                            f"Account- {profile.account_name}, Password- {profile.account_password}, Password Length- {profile.password_length}")
                        print("")
                else:
                    print("")
                    print("You dont seem to have any profiles saved yet")
                    print("")

            elif short_code == "fp":
                print("Enter the account you want to find the password for")

                account_name = input()
                if check_existing_profile(account_name):
                    search_profile = find_profile(account_name)
                    print("_" * 20)
                    print(f"{search_profile.account_name}")
                    print(f"Password - {search_profile.account_password}")
                    print("")
                    print(
                        f"Password Length - {search_profile.password_length}")
                    print("_" * 20)
                else:
                    print("That profile does not exist")
                    print("")

            elif short_code == "ex":
                print("")
                print(
                    "*" * 10 + " Thank you! Bye :) " + "*" * 10)
                print("")
                break


if __name__ == '__main__':
    main()
