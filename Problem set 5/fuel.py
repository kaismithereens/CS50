"""
In a file called fuel.py, reimplement Fuel Gauge from Problem Set 3, restructuring your code per the below, wherein:

->convert expects a str in X/Y format as input, wherein each of X and Y is an integer,
and returns that fraction as a percentage rounded to the nearest int between 0 and 100, inclusive.

If X and/or Y is not an integer, or if X is greater than Y, then convert should raise a ValueError.
If Y is 0, then convert should raise a ZeroDivisionError.

->gauge expects an int and returns a str that is:
"E" if that int is less than or equal to 1,
"F" if that int is greater than or equal to 99,
and "Z%" otherwise, wherein Z is that same int.
"""

def main():
    user_input = 0
    while user_input == 0 or user_input.find("/") == -1:
        user_input = input("X/Y:")
        continue
    p = -1
    try:
        p = convert(user_input)
    except ValueError:
        pass
    fuel_left = gauge(p)
    print(fuel_left)



def convert(fraction):
    x = 0
    y = 0
    try:
        x, y = fraction.split("/")
    except ValueError:
        print("Enter 2 values separated by /")
        raise

    try:
        x = int(x)
        y = int(y)
    except ValueError:
        raise

    if x > y:
        print("X greater than Y")
        raise ValueError

    try:
        percentage = (float)(x / y) * 100
        if percentage != int(percentage):
            percentage = percentage + 0.5
            percentage = int(percentage)
        else:
            percentage = int(percentage)
    except ZeroDivisionError:
        print("Y can not be zero")
        raise

    return percentage

def gauge(percentage):
    if 1<percentage<99:
        return f"{percentage}%"
    elif 0<= percentage<=1:
        return f"E"
    elif percentage>=99:
        return f"F"
    else:
        return f"Enter two numbers, x must be lesser than y"



if __name__ == "__main__":
    main()





