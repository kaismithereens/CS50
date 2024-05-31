"""
In a file called plates.py, reimplement Vanity Plates from Problem Set 2,
restructuring your code per the below, wherein is_valid still expects a str as input and
returns True if that str meets all requirements and False if it does not,
but main is only called if the value of __name__ is "__main__":
"""
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

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
    #are the first two characters uppercase letters?
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


def is_valid(s):
    if lenght_is_valid(s) == True and fist_two_letters(s)==True and no_special_chars(s)== True and numbers_check(s)==True:
        return True
    else:
        return False


if __name__ == "__main__":
    main()

