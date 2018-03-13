#!/usr/bin/env python
#
## Probe to access data from coinmarketcap.com

from coinmarketcap import Market

__author__ = "Patrick Dyroff"
__credits__ = "Nir Kabessa"
__version__ = "1.0"
__email__ = "pd2519@columbia.edu"
__status__ = "Prototype"

market = Market()
bucket = 0

currency = ("Add Currency to the bucket: (enter empty string to terminate)\n")

while (currency!=""):
    currency = input("Add Currency to the bucket: (enter empty string to terminate)\n")
    data = market.ticker(currency)
    bucket = float(data[0][u'market_cap_usd'])
    #data2 = market.ticker("bitcoin")


print(bucket)

indexCurrency = input("What currency would you like to compare?\n")

indexData = market.ticker(indexCurrency)

indexValue = float(indexData[0][u'market_cap_usd'])

index = indexValue / bucket


print("\nIndex/Coin: {}".format(index))
print("Index Mkt Cap: ${}".format(int(bucket)))
print("Coin Mkt Cap: ${}".format(int(indexValue)))


