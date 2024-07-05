import re
import pytest
from um import count

def test_count():
    assert count("hello, um, world") == 1
    assert count("yummy") == 0
    assert count("  um") == 1
    assert count("blah, UM") == 1
    assert count("um, , UM, hahdum") == 2
    assert count("UMUMUM blah") == 0

def test_mumble():
    assert count("Um, thanks, um, regular expressions make sense now.") == 2

def test_questions():
    assert count("Um? Mum? Is this that album where, um, umm, the clumsy alums play drums?") == 2

def test_threedots():
    assert count("This is, um... CS50.") == 1

def test_three_dots():
    assert count("Um... what are regular expressions?") == 1

def test_single():
    assert count("um") == 1

