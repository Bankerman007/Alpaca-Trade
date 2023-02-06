import alpaca_trade_api as tradeapi
import os
from alpaca_trade_api.rest import TimeFrame
from datetime import datetime, timedelta
from business_calendar import Calendar, MO, TU, WE, TH, FR
import pandas as pd

key = os.environ['API_KEY']
secret = os.environ['SECRET_KEY']
alpaca_endpoint = os.environ['APCA_API_BASE_URL']
api = tradeapi.REST(key,secret,alpaca_endpoint,)

symbol = 'TSLA'
timeframe_day = "1Day"
timeframe_hour= "1Hour"
current_time= datetime.now()
day_minus_one = datetime.today() - timedelta(days=1)
h_comma= day_minus_one.strftime('%Y,%d,%m')
h_dash= day_minus_one.strftime('%Y-%m-%d')
date1 = h_comma
cal = Calendar(workdays=[MO,TU,WE,TH,FR], holidays=['2023-01-16','2023-02-20','2023-04-07','2023-05-29','2023-06-19','2023-07-04','2023-09-04','2023-11-23','2023-12-25'])
date2 = cal.addbusdays(date1, -5)
date2=(date2.strftime('%Y-%m-%d'))

now = h_dash
end = h_dash
start = date2



def list_any_positions():
    quantity= api.list_positions()
    return quantity

def closing_bars():
    closing_bars = api.get_bars(symbol,timeframe_day,start,end,limit=5).df
    return closing_bars

def hourly_close_bars():
    scraper = pd.read_html('https://money.cnn.com/quote/quote.html?symb=TSLA')
    conc = pd.concat(scraper)
    row = conc.head(1)
    row_price = row.iloc[0,0]
    hourly_bars = (row_price[0:6])
    return hourly_bars

def place_order():
    api.submit_order(symbol, 1, 'buy', 'market','gtc')

def exit_trade_order():
    api.submit_order(symbol, 1, 'sell', 'market','gtc')
   
def purchase_price():
    purchase_price = (api.get_position(symbol).avg_entry_price)
    return float(purchase_price)

# def order_history():
#     orders= api.list_orders(status="closed", limit=100).df
#     file=open(r'C:\Users\scott\Documents\Python\Trading_bot\closed_orders.txt', 'a')
#     file.write(f'{orders} -. \n' )

def get_profits():
    data= api.get_portfolio_history(period="3M",timeframe="1D").df
    profits =data["profit_loss"]
    return profits



