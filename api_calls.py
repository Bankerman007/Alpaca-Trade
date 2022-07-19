import alpaca_trade_api as tradeapi
import os
from alpaca_trade_api.rest import TimeFrame

class Api_call:
    """API call information to be used by trade criteria calculations file"""
    
    key = os.environ['ALPACA_KEY']
    secret = os.environ['ALPACA_SECRET']
    alpaca_endpoint = 'https://paper-api.alpaca.markets'
    api = tradeapi.REST(key,secret,alpaca_endpoint)

    def __init__(self,name,symbol):
        self.name = name
        self.symbol = symbol

    @staticmethod
    def list_any_positions():
        quantity= Api_call.api.list_positions()
        #print(bool(quantity))
        return quantity

    @staticmethod
    def closing_bars(symbol):
        closing_bars = Api_call.api.get_bars(symbol,TimeFrame.Day).df
        return closing_bars

    @staticmethod
    def hourly_close_bars(symbol):
        hourly_bars = Api_call.api.get_bars(symbol,TimeFrame.Hour,limit=10).df
        return hourly_bars

    @staticmethod
    def place_order(symbol):
        Api_call.api.submit_order(symbol, 1, 'buy', 'market','gtc')
        print(f'Processing the order for {symbol}.')
        print(f'Current open positions is open.')
    
    @staticmethod
    def exit_trade_order(symbol):
        Api_call.api.submit_order(symbol, 1, 'sell', 'market','gtc')
        print(f'Processing the order for {symbol}.')
        print(f'Positions is closed.')
    

    @staticmethod
    def purchase_price(symbol):
        entry_price = (Api_call.api.get_position(symbol).avg_entry_price)
        #print(f'purchase price is {entry_price}')
        return entry_price


