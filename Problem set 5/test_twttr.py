"""
Then, in a file called test_twttr.py, implement one or more functions that collectively test your implementation
of shorten thoroughly, each of whose names should begin with test_ so that you can execute your tests with:

pytest test_twttr.py
"""
from twttr import shorten

def test_empty():
    assert shorten("") == ""

def test_capital_letters():
    assert shorten("HELLO") == "HLL"

def test_lowercase():
    assert shorten("hello") == "hll"

def test_no_change():
    assert shorten("bcdfgh") == "bcdfgh"

def test_number():
    assert shorten("Hello1") == "Hll1"

def test_punctuation():
    assert shorten("Hello!") == "Hll!"

