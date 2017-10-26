# Andrew McNally CryptoTracker
# 10/25/2017
import requests

response = requests.get("https://api.gdax.com/products/ETH-USD/book")
print(response.json())