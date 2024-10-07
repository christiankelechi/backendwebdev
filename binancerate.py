import requests

url = "https://min-api.cryptocompare.com/data/price"
params = {
    'fsym': 'USDT',
    'tsyms': 'NGN',
    'e': 'Binance'
}

response = requests.get(url, params=params)
data = response.json()

print(f"BTC/USDT Price from Binance: {data['NGN']}")
