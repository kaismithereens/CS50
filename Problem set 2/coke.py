"""
In a file called coke.py, implement a program that prompts the user to insert a coin, one at a time,
each time informing the user of the amount due. Once the user has inputted at least 50 cents,
output how many cents in change the user is owed.
Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.
"""

def is_allowed(money):
    if money == 10 or money == 25 or money == 5:
        return True
    else:
        return False

total_amount = 0
cost = 50
#print(f"Amount due: ${cost}")
while total_amount < 50:
    my_coin = int(input("Insert Coin: "))
    if is_allowed(my_coin):
        total_amount = total_amount + my_coin
        still_need = cost - total_amount
        if total_amount >= 50:
            change = -1 * still_need
            print(f"Change Owed: {change}\n")
        else:
            print(f"Amount Due: {still_need}\n")
    else:
        print(f"Amount Due: {cost - total_amount}\n")
        continue




