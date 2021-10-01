import requests

data = requests.get('https://www.coingecko.com/en/coins/bitcoin')

print(data.text)