class Student:
    #initialize the object
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house

def get_student():
    """
    student = Student()
    student.name = input("Name: ")
    student.house = input("House: ")
    """

    name = input("Name: ")
    house = input("House: ")
    """
    try:
        return Student(name, house)
    except ValueError:
        ...
    """
    return Student(name, house)

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")


if __name__ == "__main__":
    main()

