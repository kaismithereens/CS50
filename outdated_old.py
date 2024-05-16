"""
In a file called outdated.py, implement a program that prompts the user for a date, anno Domini,
in month-day-year order, formatted like 9/8/1636 or September 8, 1636,
wherein the month in the latter might be any of the values in the list below.
Then output that same date in YYYY-MM-DD format.
If the user’s input is not a valid date in either format, prompt the user again.
Assume that every month has no more than 31 days; no need to validate whether a month has 28, 29, 30, or 31 days.
"""

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def month_translate(old_month):
    if old_month in months:
        return old_month
    elif int(old_month)<= 12:
        return months[int(old_month) - 1]
    else:
        print("This is not a month.")

def day_translate(old_day):
    day = int(old_day)
    if day > 31:
        print("A month has only 31 day.")

old_date = input("Date: ")
try:
    #print("Date is in format: MM/DD/YYYY")
    data = old_date.split("/")
    old_month = data[0]
    old_day = data[1]
    old_year = data[2]
    #print(data)
    #print(old_year)
    print(month_translate(old_month))
except:
    #print("Date is in another format: MM DD, YYYY")
    data = old_date.split(",")
    first_part = data[0]
    second_part = data[1]
    month_and_day =first_part.split(" ")
    the_month = month_and_day[0]
    the_day = month_and_day[1]
    print(month_translate(the_month))
