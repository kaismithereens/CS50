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
def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if lenght_is_ok(s) and start_letters(s) and no_special_chars(s) and numbers_at_the_end(s) and check_first(s):
        return True
    else:
        return False

def start_letters(s):
    if "A" <= s[0] <= "Z" and "A" <= s[1] <= "Z":
        return True
    else:
        return False

def lenght_is_ok(s):
    if 2 <= len(s) <= 6:
        return True
    else:
        return False

def numbers_at_the_end(s):
    if "0" <= s[-1] <= "9":
        return True
    else:
        return False
"""
def first_number_not_zero(s):
    for letter in s:
        if letter.isdigit() == False:
            continue
        else:
            if letter != "0":
                break
            return True
    return False
"""
def no_special_chars(s):
    if s.isalnum():
        return True
    else:
        return False


def check_first(s):
    for letter in s:
        if letter.isdigit() == False:
            continue
        elif letter == "0":
                return False
        else:
            return True

main()

