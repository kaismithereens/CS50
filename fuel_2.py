"""
In a file called fuel.py, implement a program that prompts the user for a fraction, formatted as X/Y,
wherein each of X and Y is an integer, and then outputs, as a percentage rounded to the nearest integer,
how much fuel is in the tank.
If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty.
And if 99% or more remains, output F instead to indicate that the tank is essentially full.

If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again.
(It is not necessary for Y to be 4.)
Be sure to catch any exceptions like ValueError or ZeroDivisionError.
"""

def main():
    a, b = 0, 0
    while a >= b or b == 0:
        my_input = input("X/Y:")
        try:
            a, b = separate_XY(my_input)
        except ValueError:
            print("Enter 2 values separated by /")
            continue
        try:
            answer = divide_and_conquer(a, b)
        except ZeroDivisionError:
            print("b cannot be zero!")
            continue
        except TypeError:
            continue

    if answer == "F" or answer == "E":
        print(answer)
    else:
        print(answer, "%", sep="")



def separate_XY(user_input):

    x, y = user_input.split("/")

    try:
        x = int(x)
        y = int(y)
        #print("X is: ", x,"\nY is: ", y)
    except ValueError:
        print("Enter 2 numbers")
    return x, y

def divide_and_conquer(a, b):

    percentage = (a / b) * 100

    if a<b and 1<percentage<99:
        return int(percentage)
    elif a<b and percentage<=1:
        return "E"
    elif a<=b and percentage>=99:
        return "F"
    else:
        print("Enter two numbers, x must be lesser than y")
main()


