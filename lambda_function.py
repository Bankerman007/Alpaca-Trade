import alpaca_trade_api as tradeapi
from alpaca_trade_api.rest import TimeFrame


key = 'PK27T54I07BJ6BJKVF40'
secret = 'vroOWJYxvaAk8nTl6Jk1IxGB9KuQN2XxCkGqchdH'
alpaca_endpoint = 'https://paper-api.alpaca.markets'
api = tradeapi.REST(key,secret,alpaca_endpoint)


def lambda_handler(event=None, content=None):
    simple_test()

def simple_test():
    price = api.get_bars('TWTR',TimeFrame.Day,'2022-04-29','2022-04-29',limit=1).df
    print(price)
    output = price['close'].sum()
    print(output)

lambda_handler(1,5)


