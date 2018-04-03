# Password Locker
This is an application that allows us to generate and store passwords for various accounts.


## Specs
The user can:
1. To create an account with details - log in and password
2. Generate a password for a new credential
3. Store existing login credentials

## Prerequisites
Python3.6

## Setup Instructions
1. You need to have installed python3, to do that, run the following code on your terminal:
```
$ sudo apt-get install pyhton3
```
2. Clone the app to your local computer.
3. open your cloned folder through the terminal.
4. run the run.py file using terminal.
5. make sure you are in the cloned folder.
```
python3.6 run.py
```

## Usage
- You can create a password profile. This basically means noting down the account you want a password for. Use:
  * np - to create a password profile. The application will automatically save your profile


- You have the option of generating a password using our random password generator or writing down one of your won.
  * g - for using our random password generator.
  * m - to write down one of your own. We will save the password for you.


- You can search a password by account name. E.g if your want to find your save profile for Facebook. Use
  * fp- for find profile
  * Input the name "Facebook" for Example
  * Program will display your account name plus the password

- You can also display all the profiles saved. Enter
  * dp - for displaying all your save profiles.
  * All you saved password profiles with the passwords will be displayed.

  - Use "ex" to exit the program.

## Running tests
Run the following in your terminal,in the cloned folder
1. for credential class tests:
 ```
 python3.6 credentials_test.py
 ```
.
2. for user class tests:
```
python3.6 test_user.py
```
## Support and contact details
Contact me on my email; ykagondu@gmail.com with questions, comment and additions that can be added to the project.

## Bugs
There is no database to support the app so once you exit or log out of a session you loose all the credentials and created user.
You have to create a new user for every session. You can still use the default login but if you exit the app, you will still loose all the credentials you created.
Presence of failed tests.
Kindly contact me if more bugs are found.

## License
MIT License.
copyright Yvonne Kagondu 2018
