import requests
import config

class Api:

    @staticmethod
    def get_price(base, quote, amount):
        headers = {'authorization': 'Apikey ' + config.urls.API_KEY}
        url = f'https://min-api.cryptocompare.com/data/price?fsym={base}&tsyms={quote}, {base, quote}!'
        r = requests.get(url,  headers=headers)
        return r.json()[quote] * amount
