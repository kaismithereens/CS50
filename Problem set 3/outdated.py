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
def number_of_days(s):
    if 1<=int(s)<=31:
        return True
    else:
        return False

def number_of_months(s):
    if 1<=int(s)<=12:
        return True
    else:
        return False

def month_check(s):
    if 1<=int(s)<10:
        s = "0" + s
    return s

def day_check(s):
    if 1<=int(s)<10:
        s = "0" + s
    return s

def main():
    my_months = []
    for i in range(12):
        my_months.append(i+1)

    months_dict = dict(zip(months, my_months))

    while True:
        input_date = input("Date:")
        if input_date.find("/")!= -1:
            try:
                m, d, y = input_date.split("/")
                m = m.strip()
                d = d.strip()
                y = y.strip()
                if number_of_days(d)==True and number_of_months(m)==True:
                    new_m = month_check(m)
                    new_d = day_check(d)
                    print(f'{y}-{new_m}-{new_d}',sep="",end="")
                    break
                else:
                    continue
            except ValueError:
                continue
        elif input_date.find(",")!=-1:
            try:
                first_part, yy = input_date.split(",")
                mm, dd = first_part.split(" ")
                if mm not in months:
                    print("Not a valid month!")
                    continue
                else:
                    MM = months_dict[mm]
                    MM = str(MM)
                if number_of_days(dd)==True:
                    new_dd = day_check(dd)
                    new_MM = month_check(MM)
                    print(f'{yy}-{new_MM}-{new_dd}',sep="",end="")
                    break
                else:
                    continue

            except ValueError:
                continue

main()

