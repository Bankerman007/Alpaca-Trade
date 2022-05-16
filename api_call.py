import alpaca_trade_api as tradeapi
import os

class Api_call:
    """API call information to be used by services"""

    key = os.environ['ALPACA_KEY']
    secret = os.environ['ALPACA_SECRET']
    alpaca_endpoint = 'https://paper-api.alpaca.markets'
    api = tradeapi.REST(key,secret,alpaca_endpoint)
    
    def __init__(self,name,symbol):
        self.name = name
        self.symbol = symbol