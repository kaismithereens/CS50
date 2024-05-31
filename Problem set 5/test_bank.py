"""
Then, in a file called test_bank.py, implement three or more functions that collectively test your implementation
of value thoroughly, each of whose names should begin with test_ so that you can execute your tests with:

pytest test_bank.py
"""

from bank import value

def test_hello():
    assert value("hello") == 0

def test_h():
    assert value("hi") == 20

def test_no_h():
    assert value("uhm") == 100

def test_number():
    assert value("0") == 100

def test_empty():
    assert value("") == 100
    
def test_uppercase():
    assert value("HELLO") == 0

