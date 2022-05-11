import alpaca_trade_api as tradeapi
from alpaca_trade_api.rest import TimeFrame
import os
from orders import Place_Orders


key = os.environ['ALPACA_KEY']
secret = os.environ['ALPACA_SECRET']
alpaca_endpoint = 'https://paper-api.alpaca.markets'
api = tradeapi.REST(key,secret,alpaca_endpoint)


def lambda_handler(event=None, content=None):
    simple_test()

def simple_test():
    price = api.get_bars('TWTR',TimeFrame.Day,'2022-04-29','2022-04-29',limit=1).df
    print(price)
    output = price['close'].sum()
    print(output)
    quantity= Place_Orders.api.list_positions()
    if quantity == []:
        print(f'buy!')
    else:
        print(f'already have a position open')
        print(quantity)
    
    print(quantity)
lambda_handler(1,5)


