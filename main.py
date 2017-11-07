# Andrew McNally CryptoTracker
# 10/25/2017
# Note: limited to 3 requests per sec
import gdaxAPI
import time
import requests
import sys

price = gdaxAPI.getPrice('ETH')

capital = 10000;
shares = [];  # find better name

shares[0] = {}
shares['price'] = price
shares['coins'] = capital/price


# buy everything.

while(1):
	time.sleep(4)
	newPrice = gdaxAPI.getPrice('ETH')
	

