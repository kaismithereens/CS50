"""
In Season 5, Episode 23 of NUMB3RS, a supposed IP address appears on screen, 275.3.6.28,
which isn’t actually a valid IPv4 (or IPv6) address.

An IPv4 address is a numeric identifier that a device (or, on TV, hacker) uses to communicate on the internet,
akin to a postal address in the real world, typically formatted in dot-decimal notation as #.#.#.#.
But each # should be a number between 0 and 255, inclusive. Suffice it to say 275 is not in that range!
If only NUMB3RS had validated the address in that scene!

In a file called numb3rs.py, implement a function called validate that expects an IPv4 address as input as a str and
then returns True or False, respectively, if that input is a valid IPv4 address or not.

Structure numb3rs.py as follows, wherein you’re welcome to modify main and/or implement other functions as you see fit,
but you may not import any other libraries. You’re welcome, but not required, to use re and/or sys.
"""
import re
import sys


def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):

    if address := re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip):
        if 0<=int(address.group(1))<256 and 0<=int(address.group(2))<256 and 0<=int(address.group(3))<256 and 0<=int(address.group(4))<256:
            return True
        else:
            return False
    return False


if __name__ == "__main__":
    main()

