from trade_criteria_calcs import stocks_trade_criteria, stocks_last_hours_close, stocks_last_fiveday_avg_close
from api_calls import list_any_positions, exit_trade_order, place_order, purchase_price
import datetime
from python_to_postgres import save_to_db

time_includes_milli = datetime.datetime.now()
time_without_leading_zero=time_includes_milli.isoformat(timespec="seconds").replace("-0", "-")
time_acceptalbe_format= time_without_leading_zero.replace("T"," ")

def submit_stock_orders():
    
    acceptable_trade_criteria = stocks_trade_criteria()
    current_price = stocks_last_hours_close()
    quantity= list_any_positions()
                
    if bool(quantity):
        purchase_point = purchase_price() 
        if float(current_price) - float(purchase_point) >= 4.00:
            exit_trade_order()
            new_data= (f'"{time_acceptalbe_format}","Position exited.",{current_price},{stocks_last_fiveday_avg_close()},{purchase_point}')
            save_to_db(eval(new_data))
        else:
            new_data= (f'"{time_acceptalbe_format}","No trades executed.",{current_price},{stocks_last_fiveday_avg_close()},{purchase_point}')
            save_to_db(eval(new_data))

    elif not bool(quantity):
        if acceptable_trade_criteria and not bool(quantity):
            place_order()
            new_data= (f'"{time_acceptalbe_format}","Position is now open.",{current_price},{stocks_last_fiveday_avg_close()},{purchase_point}')
            save_to_db(eval(new_data))  

        else:
            print(f'price point not acceptable to execute any trades') 
         
            new_data= (f'"{time_acceptalbe_format}","No trades executed during API call.",{current_price},{stocks_last_fiveday_avg_close()},None')
            save_to_db(eval(new_data))
