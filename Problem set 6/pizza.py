"""
In a file called pizza.py, implement a program that expects exactly one command-line argument,
the name (or path) of a CSV file in Pinocchio’s format, and outputs a table formatted as ASCII art using tabulate,
a package on PyPI at pypi.org/project/tabulate.

Format the table using the library’s grid format.
If the user does not specify exactly one command-line argument, or
if the specified file’s name does not end in .csv, or
if the specified file does not exist, the program should instead exit via sys.exit.
"""
import sys
import csv
from tabulate import tabulate

def get_argument():
    if len(sys.argv) == 2:
        return sys.argv[1]
    elif len(sys.argv) < 2:
        sys.exit("Too few arguments")
    else:
        sys.exit("Too many arguments")

def valid_argument(s):
    if s.endswith(".csv"):
        return True
    else:
        return False

def main():
    try:
        my_filename = get_argument()
        if valid_argument(my_filename) == True:
            with open(my_filename) as table:
                reader = csv.reader(table)
                h = next(reader, None)
                my_row = []
                print(type(h))
                for row in reader:
                    my_row.append(row)
                print(tabulate(my_row, h, tablefmt="grid"))
        else:
            sys.exit("Not a csv file")
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()

