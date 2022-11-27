
import api_key
import requests

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

headers = {
    'X-CMC_PRO_API_KEY' : api_key.API_KEY,
    'Accepts' : 'application/json'
}

currency = api_key.CCY

parameters_total_mc = {
    'convert': currency
}
json = requests.get(url, params=parameters_total_mc, headers=headers).json()
coins = json['data']
for x in coins:
    print(x['quote']['BTC']['price'])

