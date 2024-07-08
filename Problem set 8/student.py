
"""
name = input("What is your name?")
house = input("What is your house?")
"""

def get_name():
    return input("Name")

def get_house():
    return input("House")

"""
def main():
    name = get_name()
    house = get_house()
    print(f"{name} from {house}")
"""

def get_student():
    name = input("Name: ")
    house = input("House: ")
    #return name, house
    return [name, house]

def main():
    #name, house = get_student()
    student = get_student()
    if student[0] == "Padma":
        #tuple object does not support item assignment
        student[1] = "Ravenclaw"
    #print(f"{name} from {house}")
    print(f"{student[0]} from {student[1]}")


if __name__ == "__main__":
    main()

