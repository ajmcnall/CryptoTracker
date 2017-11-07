import requests
import sys

def getPrice(coin):
	response = requests.get("https://api.gdax.com/products/"+ coin + "-USD/book")
	responseJson = response.json()
	# First item in array is ~current price
	price = float(responseJson['bids'][0][0])
	print("Price of " + coin + " is " + responseJson['bids'][0][0] + ".")
	sys.stdout.flush() # if using timeouts, stdout must be flushed
	return price
