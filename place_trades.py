from stocks_to_trade import actual_stocks
from stock_prices import Stock_Methods
from api_call import Api_call


class Place_Orders(Api_call):
    """Enters or exits positions based on trade criteria"""
    
    def submit_stock_orders(self):
        acceptable_trade_criteria = Stock_Methods.stocks_trade_criteria(self.symbol)
        current_price = Stock_Methods.stocks_last_hours_close
        
        
        quantity= Place_Orders.api.list_positions()
        if quantity == []:
            if acceptable_trade_criteria and quantity == []:
                self.api.submit_order(self.symbol, 1, 'sell', 'market','gtc')
                print(f'Processing the order for {self.name}.')
                open = Place_Orders.api.get_position(self.symbol)
                print(f'Current open positions is {open}.')
        if acceptable_trade_criteria == False:
            print(f'price too low to execute')    
        
        if quantity != []:
            purchase_price = (Place_Orders.api.get_position(self.symbol).avg_entry_price)        
            if float(purchase_price) - float(current_price) >= 0.50:
                    self.api.submit_order(self.symbol, 1, 'buy', 'market','gtc')
                    print(f'position exited')


if __name__ == '__main__':
    for s in actual_stocks:
        Place_Orders.submit_stock_orders(s)
