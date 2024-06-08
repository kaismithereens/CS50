import sys
import csv

def read_arguments():
    if len(sys.argv) == 3:
        input_csv = sys.argv[1]
        output_csv = sys.argv[2]
        return input_csv, output_csv
    else:
        sys.exit("Provide 2 arguments: input and output file name!")

def main():
    my_list = []
    try:
        my_input, my_output = read_arguments()
        with open(my_input) as file_r:
            reader = csv.reader(file_r)
            header = next(reader, None)

            for row in reader:

                name, house = row[0], row[1]
                lname, fname = name.split(",")
                my_list.append({"fname": fname, "lname": lname, "house": house})

        with open(my_output, 'w') as file_w:
            writer = csv.DictWriter(file_w, fieldnames=["firstname", "lastname", "house"])
            writer.writeheader()
            for row in my_list:
                #print(row['lname'])
                writer.writerow({"firstname": row['fname'], "lastname": row['lname'], "house": row['house']})

    except FileNotFoundError:
        sys.exit("No output file")

main()


