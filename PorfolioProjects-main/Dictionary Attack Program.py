import random
import pyautogui as pyautogui
import string

# Declaring Variables
chars = string.printable
chars_list = list(chars)
password = pyautogui.password("Enter a password: ")
guess_password = ""  # stores guessed passwords
Common_Passwords = open('Password Dictionary.txt', 'r+')

# read file content
readfile = Common_Passwords.read()

# checking condition for string found or not
if password in readfile:
	print('The password is ', password, '')
else:
	print("default to brute force")

#Block of code for brute force attacks. Need to make into fuction
# while(guess_password != password):
#     guess_password = random.choices(chars_list, k=len(password))
#
#     print("<==================" + str(guess_password) + "==================>")
#
#     if(guess_password == list(password)):
#         print("Your password is: " + "".join(guess_password))
#         break

# closing a file
Common_Passwords.close()


