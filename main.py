from trade_criteria_calcs import Trade_decisions
from api_calls import Api_call


class Stocks_and_orders:
    """Enters or exits positions based on trade criteria"""
    
    def __init__(self,name,symbol) -> None:
        self.name = name
        self.symbol = symbol
    
    def submit_stock_orders(self):
        acceptable_trade_criteria = Trade_decisions.stocks_trade_criteria(self.symbol)
        #print(acceptable_trade_criteria)
        current_price = Trade_decisions.stocks_last_hours_close(self.symbol)
        quantity= Api_call.list_any_positions()
        
                
        if bool(quantity):
            purchase_price = Api_call.purchase_price(self.symbol) 
            if float(current_price) - float(purchase_price) >= 0.25:
                Api_call.exit_trade_order(self.symbol)
        
        elif not bool(quantity):
            if acceptable_trade_criteria and not bool(quantity):
                Api_call.place_order(self.symbol)
                  
        else:
            print(f'price point not acceptable to execute any trades') 
    
       
