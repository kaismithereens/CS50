"""
Suppose that you’d like to implement a cookie jar in which to store cookies. In a file called jar.py, implement a class called Jar with these methods:

__init__ should initialize a cookie jar with the given capacity, which represents the maximum number of cookies that can fit in the cookie jar.
If capacity is not a non-negative int, though, __init__ should instead raise a ValueError.

__str__ should return a str with n 🍪, where n is the number of cookies in the cookie jar.
For instance, if there are 3 cookies in the cookie jar, then str should return "🍪🍪🍪"

deposit should add n cookies to the cookie jar.
If adding that many would exceed the cookie jar’s capacity, though, deposit should instead raise a ValueError.

withdraw should remove n cookies from the cookie jar. Nom nom nom.
If there aren’t that many cookies in the cookie jar, though, withdraw should instead raise a ValueError.

capacity should return the cookie jar’s capacity.
size should return the number of cookies actually in the cookie jar, initially 0.
"""
import sys

class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        cookie = "🍪"
        return cookie * self.size

    def deposit(self, n):
        if self.size <= self.capacity -n:
            self.size += n
            return self.size
        else:
            raise ValueError("Max capacity reached!")



    def withdraw(self, n):
        if self.size >= n:
            self.size -= n
        else:
            raise ValueError("Not enough cookies in the cookie jar!")


    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("Capacity negative!")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size

def main():
    jar = Jar()
    jar.deposit(0)
    print(jar)

if __name__ == "__main__":
    main()

