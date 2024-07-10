class Student:
    #initialize the object
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        #define __str__ method that enables you to print student object
        return f"{self.name} from {self.house}"

    def charm(self):
        match self.patronus:
            case "Stag":
                return ":)"
            case "Otter":
                return ":(>)"
            case "Jack Russel terrier":
                return ":-/"
            case _:
                return "/"

def get_student():

    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    return Student(name, house, patronus)

def main():
    student = get_student()
    #print(student)
    #prints <__main__.Student object at 0x7869e2b23620> -> location, when there is no __str__ method
    print("Expecto patronum!")
    print(student.charm())

if __name__ == "__main__":
    main()

