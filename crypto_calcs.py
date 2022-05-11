from alpaca_trade_api.rest import TimeFrame
from api_info import Api 

class Crypto(Api):
        
    def cryptos_last_weeks_avg_close(self):
        closing_prices_crypto = Crypto.api.get_crypto_bars(self,TimeFrame.Day,'2022-04-04','2022-04-08').df
        sum_closing_prices= closing_prices_crypto['close'].sum()
        weekly_average = sum_closing_prices/5
        print(self,weekly_average)
        return weekly_average

    def cryptos_last_hours_close(self):
        price = Crypto.api.get_crypto_bars(self,TimeFrame.Hour,limit=1).df
        current_price_crypto = price['close'].sum()
        print(self,current_price_crypto)
        return current_price_crypto
         
    def cryptos_trade_criteria(self):
        lw = int(float(Crypto.cryptos_last_weeks_avg_close(self)))
        lh = int(float(Crypto.cryptos_last_hours_close(self)))
        if lw > lh:
            print(True)
            return True
        else:
            print(False)   






