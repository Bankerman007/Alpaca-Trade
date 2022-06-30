from trade_criteria_calcs import Trade_decisions
from api_calls import Api_call


class Stocks_and_orders:
    """Enters or exits positions based on trade criteria"""
    
    def __init__(self,name,symbol) -> None:
        self.name = name
        self.symbol = symbol
    
    def submit_stock_orders(self):
        acceptable_trade_criteria = Trade_decisions.stocks_trade_criteria(self.symbol)
        print(acceptable_trade_criteria)
        current_price = Trade_decisions.stocks_last_hours_close(self.symbol)
        quantity= Api_call.list_any_positions()
        
                
        if not bool(quantity) == False:
            purchase_price = Api_call.purchase_price(self.symbol) 
            if float(purchase_price) - float(current_price) >= 0.25:
                Api_call.exit_trade_order(self.symbol)
        
        if not bool(quantity) == True:
            if acceptable_trade_criteria == True and not bool(quantity) == True:
                Api_call.place_order(self.symbol)
                  
        if acceptable_trade_criteria == False:
            print(f'price point not acceptable to execute any trades')    
        


if __name__ == '__main__':
    twr = Stocks_and_orders("Twitter",'TWTR')
    Stocks_and_orders.submit_stock_orders(twr)
