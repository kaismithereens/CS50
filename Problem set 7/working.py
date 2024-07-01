"""
Whereas most countries use a 24-hour clock, the United States tends to use a 12-hour clock.
Accordingly, instead of “09:00 to 17:00”, many Americans would say they work “9:00 AM to 5:00 PM” (or “9 AM to 5 PM”),
wherein “AM” is an abbreviation for “ante meridiem” and “PM” is an abbreviation for “post meridiem”,
wherein “meridiem” means midday (i.e., noon).

Conversion Table
In a file called working.py, implement a function called convert that expects a str in either of the 12-hour formats
below and returns the corresponding str in 24-hour format (i.e., 9:00 to 17:00).
Expect that AM and PM will be capitalized (with no periods therein) and that there will be a space before each.
Assume that these times are representative of actual times, not necessarily 9:00 AM and 5:00 PM specifically.

9:00 AM to 5:00 PM
9 AM to 5 PM
Raise a ValueError instead if the input to convert is not in either of those formats or
if either time is invalid (e.g., 12:60 AM, 13:00 PM, etc.).
But do not assume that someone’s hours will start ante meridiem and end post meridiem;
someone might work late and even long hours (e.g., 5:00 PM to 9:00 AM).

Structure working.py as follows, wherein you’re welcome to modify main and/or implement other functions as you see fit,
but you may not import any other libraries. You’re welcome, but not required, to use re and/or sys.
"""

import re

def convert(s):
    if working_12 := re.search(r"^(\d+)(:(\d){2})? (A|P){1}M to (\d+)(:(\d){2})? (A|P){1}M$", s):
            #print(working_12.group(0))
            starting, ending = working_12.group(0).split(" to ")
    else:
        raise ValueError

    if ":" in starting:
        ans1 = find_minutes(starting)
    else:
        ans1 = find_hour(starting)

    if ":" in ending:
        ans2 = find_minutes(ending)
    else:
        ans2 = find_hour(ending)


    return f"{ans1} to {ans2}"

def find_minutes(s):
    h, m = s.split(":")
    h = int(h)
    mi, is_PM = m.split(" ")
    mi = int(mi)

    if is_PM == "PM" and h < 12:
        h = h + 12
    elif is_PM == "AM" and h < 12:
        h = h
    elif is_PM == "PM" and h == 12:
        h = 12
    elif is_PM == "AM" and h == 12:
        h = 0
    else:
        raise ValueError("Not valid hour")

    if mi < 60:
        return f"{h:0>2}:{mi:0>2}"
    else:
        raise ValueError("Not valid minutes")

def find_hour(s):
    h, is_PM = s.split(" ")
    h = int(h)

    if is_PM == "PM" and h < 12:
        h = h + 12
    elif is_PM == "AM" and h < 12:
        h = h
    elif is_PM == "PM" and h == 12:
        h = 12
    elif is_PM == "AM" and h == 12:
        h = 0
    else:
        raise ValueError("Not valid hour 2")



    return f"{h:0>2}:00"


def main():
    print(convert(input("Hours: ")))


if __name__ == "__main__":
    main()

