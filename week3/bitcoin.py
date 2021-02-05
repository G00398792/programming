# bitcoin.py
# This program reads in a json representation from bitcoin live currency exchange rate from api.coindesk.com
# It extracts the key value for bpi - then for for the passed in currency
# Used a tuple to hold the currencys to loop over and prints out the currency plus value
# author: Barry Gardiner

import requests
url = "https://api.coindesk.com/v1/bpi/currentprice.json"
returnedData = requests.get(url)
bitCoinDict = returnedData.json()

def getBitcoinByCurrency(currency):
     bpiDict = bitCoinDict.get("bpi")
     currencydDict = bpiDict.get(currency)
     print(currency + " Rate is Currently : " + currencydDict["rate"])

mytuple = ("USD", "GBP", "EUR")
for x in mytuple:
    getBitcoinByCurrency(x)