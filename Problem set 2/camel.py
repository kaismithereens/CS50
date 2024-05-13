"""
In a file called camel.py, implement a program that prompts the user for the name of a variable in camel case
and outputs the corresponding name in snake case.
Assume that the user’s input will indeed be in camel case.
Example: firstName -> first_name
"""
def main():
    s = input("What is the variable name? ")
    result = make_snake_case(s)
    print(result)

def make_snake_case(s):
    if s.islower() == True:
        return s
    else:
        snake_case = ""
        for letter in s:
            if letter == letter.lower():
                snake_case = snake_case + letter
            else:
                snake_case = snake_case + "_" + letter.lower()
        return snake_case

main()

