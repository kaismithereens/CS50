"""
In plates.py, implement a program that prompts the user for a vanity plate and then
output Valid if meets all of the requirements or Invalid if it does not.
Assume that any letters in the user’s input will be uppercase.
Structure your program per the below, wherein is_valid returns True if s meets all requirements and False if it does not.
Assume that s will be a str.
You’re welcome to implement additional functions for is_valid to call (e.g., one function per requirement).
"""
"""
REQUIREMENTS:
“All vanity plates must start with at least two letters.”
“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
“No periods, spaces, or punctuation marks are allowed.”
"""

def lenght_is_valid(s):
    if len(s)>=2 and len(s)<=6:
        return True
    else:
        return False

def no_special_chars(s):
    if s.isalnum() == True:
        return True
    else:
        return False

def fist_two_letters(s):
    first_letters = s[0:2]
    if "A" <= first_letters[0] <="Z" and "A" <= first_letters[1] <="Z":
        return True
    else:
        return False

def numbers_check(s):
    #are there any numbers [2:END]? Are there only letters
    end_plate = s[2:]
    if end_plate.isalpha():
        return True
    else:
        for letter in end_plate:
            if letter.isalpha():
                continue
            if letter == "0":
                return False
            if end_plate.index(letter) == len(end_plate)-1:
                return True
            if end_plate[end_plate.index(letter):].isdigit():
                return True
            else:
                return False


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if lenght_is_valid(s) == True and fist_two_letters(s)==True and no_special_chars(s)== True and numbers_check(s)==True:
        return True
    else:
        return False


main()

