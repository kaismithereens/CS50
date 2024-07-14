class Wizard:
    def __init__(self, name):
         if not name:
            raise ValueError("Missing name!")
         self.name = name

class Student(Wizard):
    def __init__(self, name, house):
        #inherit the name from the super class Wizard init method
        super().__init__(name)
        """
        if not name:
            raise ValueError("Missing name!")
        self.name = name
        """
        self.house = house

        ...

class Professor(Wizard):
    def __init__(self, name, subject):
        #inherit the name from the super class Wizard init method
        super().__init__(name)
        """
        if not name:
            raise ValueError("Missing name!")
        self.name = name
        """
        self.subject = subject

        ...


wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")
professor = Professor("Severus", "Defense against the dark arts")


