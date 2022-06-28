from stock_prices import Stock_Methods
from api_call import Api_call


class Place_Orders:
    """Enters or exits positions based on trade criteria"""
    def __init__(self,name,symbol) -> None:
        self.name = name
        self.symbol = symbol
    
    def submit_stock_orders(self):
        acceptable_trade_criteria = Stock_Methods.stocks_trade_criteria(self.symbol)
        print(acceptable_trade_criteria)
        current_price = Stock_Methods.stocks_last_hours_close(self.symbol)
        quantity= Api_call.list_any_positions()
        print(quantity)
                
        if not bool(quantity) == False:
            purchase_price = Api_call.purchase_price(self.symbol) 
            if float(purchase_price) - float(current_price) >= 0.05:
                    Api_call.exit_trade_order(self.symbol)
        
        if not bool(quantity) == True:
            if acceptable_trade_criteria == True and not bool(quantity) == True:
                Api_call.place_order(self.symbol)
                  

        if acceptable_trade_criteria == False:
            print(f'price point not acceptable to execute any trades')    
        
    
               



            # if float(purchase_price) - float(current_price) >= 0.50:
            #         self.api.submit_order(self.symbol, 1, 'buy', 'market','gtc')
            #         print(f'position exited')


if __name__ == '__main__':
    twr = Place_Orders("Twitter",'TWTR')
    Place_Orders.submit_stock_orders(twr)
