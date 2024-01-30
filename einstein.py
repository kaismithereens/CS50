"""
In a file called einstein.py, implement a program in Python that prompts the user for mass as an integer (in kilograms)
and then outputs the equivalent number of Joules as an integer. Assume that the user will input an integer.
"""
mass = input("What is the mass (in kg)? ")
energy = int(mass) * pow(300000000,2)

print(energy)
