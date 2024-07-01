import re
import pytest
from working import convert

def test_convert():
    assert convert("9 AM to 11 AM") == "09:00 to 11:00"
    assert convert("9 PM to 11 AM") == "21:00 to 11:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"

def test_exceptions():
    with pytest.raises(ValueError):
        convert("9AM to 5PM")
        convert("09:00 to 17:00")
        convert("9 AM - 5 PM")
        convert("10:7 AM - 5:1 PM")
        convert("9:75 AM to 13:00 PM")


