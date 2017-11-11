# Andrew McNally CryptoTracker
# 10/25/2017
# Note: limited to 3 requests per sec
import gdaxAPI
import time
import requests
import sys

price = gdaxAPI.getPrice('ETH')

capital = 10000;
trades = [];  # find better name

trades[0] = {}
trades['type'] = 'buy'
trades['price'] = price
trades['coins'] = capital/price


# buy everything.

while(1):
	time.sleep(1)
	currentPrice = gdaxAPI.getPrice('ETH')
	for trade in trades:
		if trade.type == 'buy':
			if currentPrice > trade.price * 1.01: # 1% increase
				trade.type = 'sell'
				trade.price = currentPrice

		else if trade.type == 'sell':
			if currentPrice < trade.price * .99
				trade.type = 'buy'
				trade.price = currentPrice
				trade.coins = trade.price / currentPrice

