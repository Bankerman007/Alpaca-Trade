from alpaca_trade_api.rest import TimeFrame
from api_call import Api_call


class Stock_Methods:
    """Data for each stock that will be evaluated to trade"""
        
    def __init__(self,name,symbol) -> None:
        self.name = name
        self.symbol = symbol
    
    @staticmethod    
    def stocks_last_weeks_avg_close(symbol):
        closing_prices_stocks = Api_call.closing_bars(symbol)
        sum_closing_prices= closing_prices_stocks['close'].sum()
        weekly_average = sum_closing_prices/5
        print(f'last weeks average price {weekly_average}.')
        return weekly_average
        
    @staticmethod
    def stocks_last_hours_close(symbol):
        price = Api_call.hourly_close_bars(symbol)
        current_price_stocks = price['close'].sum()
        print(f'current stock price {current_price_stocks}')
        return current_price_stocks

    @staticmethod
    def stocks_trade_criteria(symbol):
        last_close = int(float(Stock_Methods.stocks_last_hours_close(symbol)))
        if last_close >= int(float(50.25)):
            #print(True)
            return True
        else:
            #print(False)
            return False



            



        # lw = int(float(Stock_Methods.stocks_last_weeks_avg_close(symbol)))
        # lh = int(float(Stock_Methods.stocks_last_hours_close(symbol)))
        # differnce = lw - lh
        # if lw > lh and differnce <= 0.15:
        #     print(True)
        #     return True
        # else:
        #     print(False)
        #     return False


        





