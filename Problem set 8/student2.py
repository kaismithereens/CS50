"""

def get_student():
    student = {}
    student["name"] = input("Name: ")
    student["house"] = input("House: ")
    return student
"""
def get_student():
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}

def main():
    student = get_student()
    if student['name'] == "Padma":
        student['house'] = "Ravenclaw"
    print(f"{student['name']} from {student['house']}")


if __name__ == "__main__":
    main()

