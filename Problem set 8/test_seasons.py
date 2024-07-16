import pytest
import sys
from datetime import date
from seasons import substract_dates, split_date, days_to_minutes, minutes_to_words, handle_date

def test_substraction_2digits():
    assert substract_dates(date.fromisoformat("2024-07-01")) == 15

def test_substraction_3digits():
    assert substract_dates(date.fromisoformat("2024-04-01")) == 106

def test_substraction_4digits():
    assert substract_dates(date.fromisoformat("2021-01-01")) == 1292

def test_splitting():
    assert split_date("2024-07-01") == date(2024, 7, 1)

def test_fails_with_exception():
    with pytest.raises(ValueError):
        split_date("22, 2, 2002")

def test_convert_to_minutes():
    assert days_to_minutes(1) == 1440

def test_minutes_to_words():
    assert minutes_to_words(1440) == "one thousand, four hundred forty minutes"

def test_minutes_to_words_today():
    assert minutes_to_words(0) == "zero minutes"

def test_error():
    with pytest.raises(SystemExit, match='Input date format incorrect.'):
        handle_date("February 26, 1990")




