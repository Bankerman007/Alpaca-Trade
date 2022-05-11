#from crypto_calcs import Crypto
from items_to_trade import actual_stocks #actual_cryptos
from stock_calcs import Stock_Methods
from api_info import Api



class Place_Orders(Api):
    
    def submit_stock_orders(self):
        acceptable_trade_criteria = Stock_Methods.stocks_trade_criteria(self.symbol)
        current_price = Stock_Methods.stocks_last_hours_close
        purchase_price = (Place_Orders.api.get_position(self.symbol).avg_entry_price)
        
        try:
            quantity= int(Place_Orders.api.get_position(self.symbol).qty)
        except:
            quantity = 0
            if acceptable_trade_criteria and quantity == 0:
                self.api.submit_order(self.symbol, 1, 'sell', 'market','gtc')
                print(f'Processing the order for {self.name}.')
                open = Place_Orders.api.get_position(self.symbol)
                print(f'Current open positions is {open}.')
        if float(purchase_price) - float(current_price) >= 0.50:
                self.api.submit_order(self.symbol, 1, 'buy', 'market','gtc')
                print(f'position exited')

                    
            
    # def submit_crypto_orders(self):
    #     acceptable_trade_criteria = Crypto.cryptos_trade_criteria(self.symbol)
    #     try:
    #         quantity= int(Place_Orders.api.get_position(self.symbol).qty)
    #     except Exception:
    #         quantity = 0
    #         if acceptable_trade_criteria and quantity == 0:
    #             self.api.submit_order(self.symbol, .10, 'buy', 'market','gtc')
    #             print(f'Processing the order for {self.name}.')
    #             open = Place_Orders.api.get_position(self.symbol)
    #             print(f'Current open positions is {open}.')
                


if __name__ == '__main__':
    for s in actual_stocks:
        Place_Orders.submit_stock_orders(s)
    # for c in actual_cryptos:
    #     Place_Orders.submit_crypto_orders(c)
    






#account =  api.get_account()
#print(account.status)