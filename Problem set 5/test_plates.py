"""
Then, in a file called test_plates.py, implement four or more functions that
collectively test your implementation of is_valid thoroughly,
each of whose names should begin with test_ so that you can execute your tests with:

"""

from plates import is_valid

def test_lenght():
    assert is_valid("AA1") == True
    assert is_valid("AA1234") == True
    assert is_valid("A") == False

def test_special_chars():
    assert is_valid("HEll!") == False
    assert is_valid("PL123.") == False

def test_zero():
    assert is_valid("HEll10") == True
    assert is_valid("CS05") == False

def test_numbers():
    assert is_valid("AB12AB") == False

def test_start():
    assert is_valid("777") == False

