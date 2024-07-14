import random

class Hat:

    #class variable houses
    houses = ["Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"]

    #class method sort
    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))


Hat.sort("Harry")

