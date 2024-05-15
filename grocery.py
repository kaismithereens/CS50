"""
In a file called grocery.py, implement a program that prompts the user for items, one per line,
until the user inputs control-d (which is a common way of ending one’s input to a program).
Then output the user’s grocery list in all uppercase, sorted alphabetically by item,
prefixing each line with the number of times the user inputted that item. No need to pluralize the items.
Treat the user’s input case-insensitively.
"""
grocery_list = {}
while True:
    try:
        grocery = input()
        if grocery not in grocery_list:
            grocery_list[grocery]=1
        else:
            #find grocery value, increment value + 1
            grocery_list[grocery] += 1
    except EOFError:
            break
    except KeyError:
        print("The key is not in grocery list. ")

my_list = list(grocery_list)
my_list.sort()
sorted_dict = {i: grocery_list[i] for i in my_list}

for key,value in sorted_dict.items():
     print(value, key.upper())


