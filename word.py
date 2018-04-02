#!/usr/bin/env python 3.6
from passw import User
from passw import Passwords

def create_profile(account_name, account_password, password_length):
     """
     Function to create new profile
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
    Function that finds password by account_name and returns profile
    """
    return Passwords.find_by_account(account_name)

def display_profiles():
    """
    Function that returns all the saved profiles
    """
    return Passwords.display_profiles()
