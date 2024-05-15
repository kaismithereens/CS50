import sys

x = 0
y = 0
percentage = 0

while type(x) is not int or type(y) is not int or x> y or y == 0:
    user_input = input("X/Y:")

    try:
        x, y = user_input.split("/")
    except ValueError:
        print("Enter 2 values separated by /")
        continue


    try:
        x = int(x)
        y = int(y)
    except ValueError:
        continue

    try:
        percentage = (float)(x / y) * 100
        if percentage != int(percentage):
            percentage = percentage + 0.5
            percentage = int(percentage)
        else:
            percentage = int(percentage)
    except ZeroDivisionError:
        print("Y can not be zero")
        continue

if x<y and 1<percentage<99:
    print((percentage),"%", sep="")
elif x<=y and percentage<=1:
    print("E")
elif x<=y and percentage>=99:
    print("F")
else:
    print("Enter two numbers, x must be lesser than y")

