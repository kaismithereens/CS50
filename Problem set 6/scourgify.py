"""
In a file called scourgify.py, implement a program that:

Expects the user to provide two command-line arguments:
the name of an existing CSV file to read as input, whose columns are assumed to be, in order, name and house, and
the name of a new CSV to write as output, whose columns should be, in order, first, last, and house.

Converts that input to that output, splitting each name into a first name and last name.
Assume that each student will have both a first name and last name.
If the user does not provide exactly two command-line arguments, or
if the first cannot be read, the program should exit via sys.exit with an error message.
"""
import sys
import csv

def read_arguments():
    if len(sys.argv) == 3:
        input_csv = sys.argv[1]
        output_csv = sys.argv[2]
        return input_csv, output_csv
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    else:
        sys.exit("Too many command-line arguments")


def main():

    try:
        my_input, my_output = read_arguments()

        with open(my_input) as file_r:
            reader = csv.DictReader(file_r)
            with open(my_output, "w") as file_w:
                writer = csv.DictWriter(file_w, fieldnames = ['first', 'last', 'house'])
                writer.writeheader()
                for row in reader:
                    lastname, firstname = row['name'].split(", ")
                    writer.writerow({'first': firstname.strip(), 'last': lastname.strip(), 'house': row['house'].strip()})

    except FileNotFoundError:
        sys.exit(f"Could not read {my_input}")

main()


