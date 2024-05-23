"""
In a file called bitcoin.py, implement a program that:

Expects the user to specify as a command-line argument the number of Bitcoins, that they would like to buy.
If that argument cannot be converted to a float, the program should exit via sys.exit with an error message.
Queries the API for the CoinDesk Bitcoin Price Index at https://api.coindesk.com/v1/bpi/currentprice.json, which returns a JSON object,
among whose nested keys is the current price of Bitcoin as a float.

Be sure to catch any exceptions, as with code like:
import requests

try:
    ...
except requests.RequestException:
    ...

Outputs the current cost of
 Bitcoins in USD to four decimal places, using , as a thousands separator.
 """
import requests
import sys

try:
    nr_of_bitcoins = float(sys.argv[1])
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    r = r.json()
except requests.RequestException:
    sys.exit("Error message")
except IndexError:
    print("Insert a number")
except ValueError:
    print("Not a number")

current_USD_price = r['bpi']['USD']['rate'].replace(',', '')
current_USD_price = float(current_USD_price)

buy_value = nr_of_bitcoins * current_USD_price
print(f"${buy_value:,.4f}")

