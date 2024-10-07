import requests

def get_tron_price():
    url = 'https://api.coingecko.com/api/v3/simple/price?ids=usd&vs_currencies=ngn'
    response = requests.get(url)
    data = response.json()
    tron_price = data['usd']['ngn']
    return tron_price

if __name__ == "__main__":
    price = get_tron_price()
    print(f"The current price of TRON (TRX) is: ${price} USD")
