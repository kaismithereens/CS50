"""
Assuming there are 365 days in a year, there are 525,600 minutes in that same year (because there are 24 hours in a day and 60 minutes in an hour).
But how many minutes are there in two or more years?
Well, it depends on how many of those are leap years with 366 days, per the Gregorian calendar,
as some of them could have 1,440 additional minutes.

 In fact, how many minutes has it been since you were born?
 Well, that, too, depends on how many leap years there have been since!
 There is an algorithm for such, but let’s not reinvent that wheel. Let’s use a library instead.
 Fortunately, Python comes with a datetime module that has a class called date that can help, per
 docs.python.org/3/library/datetime.html#date-objects.

In a file called seasons.py, implement a program that prompts the user for their date of birth
in YYYY-MM-DD format and then sings prints how old they are in minutes, rounded to the nearest integer,
using English words instead of numerals, just like the song from Rent, without any and between words.

Since a user might not know the time at which they were born, assume, for simplicity, that
the user was born at midnight (i.e., 00:00:00) on that date.
And assume that the current time is also midnight.
In other words, even if the user runs the program at noon, assume that it’s actually midnight, on the same date.

Use datetime.date.today to get today’s date, per docs.python.org/3/library/datetime.html#datetime.date.today.
"""
import datetime
import inflect
import sys
from datetime import date


def split_date(s):
    yy, mm, dd = s.split("-")
    yy = int(yy)
    mm = int(mm)
    dd = int(dd)
    return date(yy, mm, dd)

def substract_dates(d1):
    today = date.today()
    return abs(d1 - today).days

def days_to_minutes(d):
    minutes = d * 24 * 60
    return minutes

def minutes_to_words(min):
    p = inflect.engine()
    words = p.number_to_words(min, andword = "")
    return f"{words} minutes"

def main():

    #input date of birth
    full_date = input("Date of birth in YYYY-MM-DD: ")

    #try to split the date by "-"
    try:
        birthday_date = split_date(full_date)
    except ValueError:
        sys.exit("Input date format incorrect.")

    #get number of days from your birthday to today
    ttb = days_to_minutes(substract_dates(birthday_date))

    #print that number using words
    print(minutes_to_words(ttb).capitalize())

if __name__ == "__main__":
    main()

