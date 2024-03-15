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

def percentage(x, y):
    try:
        result = x/y
    except ZeroDivisionError:
        print("y is equal to Zero")
    else:
        return x/y

def separate_xy(f):
    try:
        x, y = 0, 0
        result = f.split("/")
        if len(result) == 2:
            x, y = result
        x = int(x)
        y = int(y)

    except ValueError:
        print("Value error")
    else:
        return x, y


def main():

    fraction = input("What is the fraction X/Y? ")
    a, b = separate_xy(fraction)
    while a >= b or b == 0:
        fraction = input("What is the fraction X/Y? ")
        a, b = separate_xy(fraction)
    print(percentage(a, b))


main()
