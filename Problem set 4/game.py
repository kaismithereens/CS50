"""
In a file called game.py, implement a program that:

Prompts the user for a level n. If the user does not input a positive integer, the program should prompt again.
Randomly generates an integer between 1 and n, inclusive, using the random module.

Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
If the guess is larger than that integer, the program should output Too large! and prompt the user again.
If the guess is the same as that integer, the program should output Just right! and exit.
"""

import random

my_level = 0
my_guess = 0

def randomize(num):
    return random.randrange(1,num)

while my_level<=0:
    try:
        my_level = int(input("Level: "))
    except ValueError:
        continue

answer = randomize(my_level)
print(answer)

while my_guess != answer:
    try:
        my_guess = int(input("Guess: "))
    except ValueError:
        continue
    if my_guess <= 0:
        continue
    elif my_guess < answer:
        print("Too small!")
        continue
    elif my_guess > answer:
        print("Too large!")
        continue
    else:
        print("Just right!")
        break




