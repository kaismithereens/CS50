class Student:

    def __init__(self, name, house):
        #initialize the student object
        """
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        """
        self.name = name
        self.house = house

    def __str__(self):
        #define __str__ method that enables you to print student object
        return f"{self.name} from {self.house}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        else:
            self._name = name

    #Getter function - gets an atribute from a class
    @property
    def house(self):
        return self._house

    #Setter function - sets a value to a class atribute
    #the name of the method/getter and setter must be different than the name of the instance variable
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"]:
            raise ValueError("Invalid house!")
        else:
            self._house = house

def get_student():

    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)

def main():
    student = get_student()
    #student.house = "House 4" -> won't work, caught as Value Error
    #studen._house = "House 4" -> will work, as _house is an instance variable
    print(student)


if __name__ == "__main__":
    main()

