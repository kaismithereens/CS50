"""
One of David’s first toys as a child, funny enough, was Little Professor, a “calculator” that would generate ten different math problems for David to solve. For instance, if the toy were to display 4 + 0 = , David would (hopefully) answer with 4. If the toy were to display 4 + 1 = , David would (hopefully) answer with 5. If David were to answer incorrectly, the toy would display EEE. And after three incorrect answers for the same problem, the toy would simply display the correct answer (e.g., 4 + 0 = 4 or 4 + 1 = 5).

In a file called professor.py, implement a program that:

Prompts the user for a level,n. If the user does not input 1, 2, or 3, the program should prompt again.
Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with
n digits. No need to support operations other than addition (+).

Prompts the user to solve each of those problems.

If an answer is not correct (or not even a number), the program should output EEE and prompt the user again,
allowing the user up to three tries in total for that problem.
If the user has still not answered correctly after three tries, the program should output the correct answer.

The program should ultimately output the user’s score: the number of correct answers out of 10.

Structure your program as follows, wherein get_level prompts (and, if need be, re-prompts) the user for a level
and returns 1, 2, or 3, and generate_integer returns a randomly generated non-negative integer with level digits
or raises a ValueError if level is not 1, 2, or 3:
"""

import random


def main():
    l = get_level()
    good_guess = 0
    for i in range(10):
        a , b = generate_integer(l)
        correct_answer = a + b
        try_nr = 1
        user_answer = 0

        while user_answer!= correct_answer and try_nr < 4:
            print(a, "+", b, "=", end = "")
            user_answer = int(input())
            try_nr = try_nr + 1
            if user_answer == correct_answer:
                good_guess = good_guess + 1
            elif try_nr == 3:
                print(correct_answer)
            else:
                print("EEE")
                
    print(good_guess)

def get_level():
    my_level = 0
    while my_level > 3 or my_level < 1:
        try:
            my_level = int(input(""))
            if my_level< 1 or my_level > 3:
                raise ValueError
        except ValueError:
            continue
    return my_level


def generate_integer(level):
    x = 0
    y = 0

    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    else:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    return x, y


if __name__ == "__main__":
    main()

