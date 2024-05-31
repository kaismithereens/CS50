"""
Then, in a file called test_fuel.py, implement two or more functions t
hat collectively test your implementations of convert and gauge thoroughly, each of whose names should begin with test_
so that you can execute your tests with:
pytest

"""
import pytest
from fuel import convert, gauge

def test_convert():
    assert convert("1/5") == 20

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(50) == "50%"

def test_passes_without_raising_ZeroDivisionError():
    with pytest.raises(Exception):
        convert("1/0")

def test_passes_without_raising_ValueError():
    with pytest.raises(Exception):
        convert("2/1")

