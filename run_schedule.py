from datetime import datetime
from main import submit_stock_orders

def run(*args):
    # today = datetime.today()
    # day = today.weekday()
    # now = datetime.now()
    # current_hour = int(now.strftime("%H%M"))
    
    # if day == 0 or 1 or 2 or 3 and current_hour >= 1100 and current_hour <= 1500:
        
    submit_stock_orders()  #This job is run Monday-Thursday 9am-3pm.
        #print(f'this ran')

run()