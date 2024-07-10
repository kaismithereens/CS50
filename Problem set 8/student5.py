class Student:

    def __init__(self, name, house):
        #initialize the student object
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house

    def __str__(self):
        #define __str__ method that enables you to print student object
        return f"{self.name} from {self.house}"


def get_student():

    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)

def main():
    student = get_student()
    print(student)


if __name__ == "__main__":
    main()

