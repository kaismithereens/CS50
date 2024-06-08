"""
in a file called lines.py, implement a program that expects exactly one command-line argument,
the name (or path) of a Python file, and outputs the number of lines of code in that file,
excluding comments and blank lines.

If the user does not specify exactly one command-line argument, or
if the specified file’s name does not end in .py, or if the specified file does not exist,
the program should instead exit via sys.exit.

Assume that any line that starts with #, optionally preceded by whitespace, is a comment.
(A docstring should not be considered a comment.)
Assume that any line that only contains whitespace is blank.
"""

import sys

def get_file_name():
    if len(sys.argv) == 2:
        file_name = sys.argv[1]
        return file_name
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    else:
        sys.exit("Too many command-line arguments")

def get_number_of_rows(filename):
    counter = 0
    with open(filename, "r") as file:
        for row in file:
            if row.lstrip()== "" or row.lstrip().startswith("#"):
                continue
            else:
                counter += 1
    return counter

def main():
    try:
        fn = get_file_name()
        try:
            left, right = fn.split(".")
        except ValueError:
            sys.exit("Not a valid extension")
        if right == "py":
            nr = get_number_of_rows(fn)
            print(nr)
        else:
            sys.exit("Not a Python file")
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()

