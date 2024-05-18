"""
In a file called adieu.py, implement a program that prompts the user for names, one per line, until the user inputs control-d.
Assume that the user will input at least one name.
Then bid adieu to those names, separating two names with one and, three names with two commas and one and, and
n names with n-1 commas and one and, as in the below:

Adieu, adieu, to Liesl
Adieu, adieu, to Liesl and Friedrich
Adieu, adieu, to Liesl, Friedrich, and Louisa
Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, and Marta
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl
"""
import inflect
p = inflect.engine()

mylist = []
name_list = []
while True:
    try:
        name = input()
        name_list.append(name)
    except EOFError:
        mylist = p.join((name_list))
        # "apple, banana, and carrot"
        print(f"Adieu, adieu, to {mylist}")
        break


