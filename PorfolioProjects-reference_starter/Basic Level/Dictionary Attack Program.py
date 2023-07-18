import random
import pyautogui as pyautogui
import string

# Declaring Variables
chars = string.printable
chars_list = list(chars)
password = pyautogui.password("Enter a password: ")
guess_password = ""  # stores guessed passwords
Common_Passwords = open('10k-most-common.txt', 'r+')


def brute_force():
    guess_password = ""  # stores guessed passwords

    while (guess_password != password):
        guess_password = random.choices(chars_list, k=len(password))

        print("<==================" + str(guess_password) + "==================>")

        if (guess_password == list(password)):
            print("Success in brute forcing the following password: " + "".join(guess_password))
            break


# read file content
readfile = Common_Passwords.read()

# checking condition for string found or not
if password in readfile:
    print('The password is in a dictionary and is: ',password, '')
else:
    brute_force()

# closing a file
Common_Passwords.close()
