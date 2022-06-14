from alpaca_trade_api.rest import TimeFrame
from api_call import Api_call


class Stock_Methods(Api_call):
    """Data for each stock that will be evaluated to trade"""

        
    def stocks_last_weeks_avg_close(self):
        closing_prices_stocks = Stock_Methods.api.get_bars(self,TimeFrame.Day,'2022-06-06','2022-06-10').df
        sum_closing_prices= closing_prices_stocks['close'].sum()
        weekly_average = sum_closing_prices/5
        print(self,weekly_average)
        return weekly_average
        

    def stocks_last_hours_close(self):
        price = Stock_Methods.api.get_bars(self,TimeFrame.Hour,limit=1).df
        current_price_stocks = price['close'].sum()
        print(self,current_price_stocks)
        return current_price_stocks

    def stocks_trade_criteria(self):
        lw = int(float(Stock_Methods.stocks_last_weeks_avg_close(self)))
        lh = int(float(Stock_Methods.stocks_last_hours_close(self)))
        differnce = lw - lh
        if lw > lh and differnce <= 0.15:
            print(True)
            return True
        else:
            print(False)
        





