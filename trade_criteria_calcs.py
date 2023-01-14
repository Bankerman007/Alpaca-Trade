from api_calls import Api_call


class Trade_decisions:
    """Evaluates prices to make trade decisions"""
        
    def __init__(self,name,symbol) -> None:
        self.name = name
        self.symbol = symbol
    
    @staticmethod    
    def stocks_last_fiveday_avg_close(symbol):
        closing_prices_stocks = Api_call.closing_bars(symbol)
        #print(f'last 5 hours average price {closing_prices_stocks}.')
        sum_closing_prices= closing_prices_stocks['close'].iloc[-5:].sum()
        dayly_average = sum_closing_prices/5
        #print(f'last 5 hours average price {closing_prices_stocks}.')
        return dayly_average
        
    @staticmethod
    def stocks_last_hours_close(symbol):
        price = Api_call.hourly_close_bars(symbol)
        #print(f'current stock price {price}')
        current_price_stocks = price['close'].iloc[-1]
        #print(f'current stock price {current_price_stocks}')
        return current_price_stocks

    @staticmethod
    def stocks_trade_criteria(symbol):
        last_five = int(float(Trade_decisions.stocks_last_fivehour_avg_close(symbol)))
        last_hour = int(float(Trade_decisions.stocks_last_hours_close(symbol)))
        differnce = last_five - last_hour
        if last_five < last_hour and differnce <= 0.25:
            print(True)
            return True
        else:
            print(False)
            return False



        # last_close = int(float(Stock_Methods.stocks_last_hours_close(symbol)))
        # if last_close >= int(float(50.25)):
        #     #print(True)
        #     return True
        # else:
        #     #print(False)
        #     return False


#Trade_decisions.stocks_last_fiveday_avg_close('TWTR')
#Trade_decisions.stocks_last_hours_close('TWTR')           






        





