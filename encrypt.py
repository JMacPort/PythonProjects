# This is the first time I have made my own program without using a template or copy/pasting. I started by creating the necessary checks for what I wanted the password to be. This requires some Googling as to what libraries are used for some of these
# like re. Once I completed the password checker, I then worked on the encryptor which again I had to find the library hashlib but it was very easy to implement. Now I needed to find something to salt the passwords in the case of duplicate entries. 
# For this, I used the string and random libraries as these were able to define a set of acceptable characters and then join them together with a predefined amount such as 4. The last piece of the program is the try/except statement which is straightforward
# uses the os library to implement the creation of a new directory such as the Hashes. I used many comments in the code to demonstrate knowing what each line does but most of the code speaks for itself. 
# To run: Open a Command Prompt type "Python3.10 encrypt.py" (without quotes) may need to change python version depending on which version you are using. 
# Note: This will only work on Windows due to the predifined path. If you would like to try on a different OS, change the paths listed in the try/except statements to whatever works for your OS. 
# Enjoy


import re
import random
import string
import hashlib
import os

#Stores the username 
user = input("What is your username? \n")
#Function to determine if password is strong enough
def PassHas():
#Creates a while loop to ensure all checks are met 
    while True:
      pw = input("What password will you try?\n")
        conditions_not_met = []
#Checks is password is 10 or more characters
        if len(pw) < 10:
            conditions_not_met.append("Password needs to be longer.")
#Checks if there is no duplicate characters
        prev_char = None
        for char in pw:
            if char == prev_char:
                conditions_not_met.append("Remove any consecutive duplicates from your password.")
                break 
            prev_char = char
#Checks if the password starts with an uppercase letter
        if not pw[0].isupper():
            conditions_not_met.append("Password needs to start with an uppercase letter.")
#Checks if there is any digits 
        if not any(char.isdigit() for char in pw):
            conditions_not_met.append("Password needs to contain a number.")
#Checks if there is a special character
        if not re.search(r'[^a-zA-Z0-9]', pw):
            conditions_not_met.append("Password needs a special character.")
#Prints "Password is valid" if all checks are met, if not will restart loop telling user to input a new password with the requirements not met. 
        if not conditions_not_met:
            print("Password is valid.")
            break
        else:
            for condition in conditions_not_met:
                print(condition)
    return pw
#Function that will encrypt the password using sha256
def encryptPass(str):
#Stores what potential characters are accepted
    characters = string.ascii_letters + string.digits + string.punctuation
#Takes 4 of the characters randomly and adds them together
    chars = ''.join(random.choice(characters) for i in range(4))
#Combines the 4 characters with the given password    
    pw = chars + str
#Encrypts the salted password with sha256 and stores the hash in a variable
    salted = hashlib.sha256(pw.encode()).hexdigest()
    try:
#Attempts to create a new file and write the username and hash to it
        with open('C:/temp/Hashes/hashes.txt', 'x') as f:
            f.write(f"{user}|{salted}")
#If file exists already it will instead append the username and hash
    except FileExistsError:
        with open('C:/temp/Hashes/hashes.txt', 'a') as f:
            f.write('\n' + f"{user}|{salted}")
#If the file cannot be created and doesn't exist it means the directory is invalid. So this will create the directory in the given path.
    except FileNotFoundError:
        try:
            os.mkdir("C:/temp/Hashes/")
            with open('C:/temp/Hashes/hashes.txt', 'x') as f:
                f.write(f"{user}|{salted}")
        except:
            print("Error cannot save file.")


encryptPass(PassHas())
