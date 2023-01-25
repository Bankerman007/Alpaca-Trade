from trade_criteria_calcs import stocks_trade_criteria, stocks_last_hours_close, stocks_last_fiveday_avg_close
from api_calls import list_any_positions, exit_trade_order, place_order, purchase_price
import datetime

def submit_stock_orders():
    file=open(r'C:\Users\scott\Documents\Python\Trading_bot\task.txt', 'a')
    acceptable_trade_criteria = stocks_trade_criteria()
    current_price = stocks_last_hours_close()
    quantity= list_any_positions()
                
    if bool(quantity):
        purchase_point = purchase_price() 
        if float(current_price) - float(purchase_point) >= 0.25:
            exit_trade_order()
            file.write(f'{datetime.datetime.now()} - Position exited at {current_price}. \n' )
        else:
            file.write(f'{datetime.datetime.now()} - Price point not acceptable to execute any trades. Market price {current_price}, Purchase Price {purchase_point}.\n' )
    
    elif not bool(quantity):
        if acceptable_trade_criteria and not bool(quantity):
            place_order()
            file.write(f'{datetime.datetime.now()} - Position is now open at {current_price}. \n' )

                
        else:
            print(f'price point not acceptable to execute any trades') 
            file.write(f'{datetime.datetime.now()} - Price point not acceptable to execute any trades. {current_price, stocks_last_fiveday_avg_close()}\n' )
    
    
