from api_calls import closing_bars, hourly_close_bars

symbol = 'TSLA'
      
def stocks_last_fiveday_avg_close():
    closing_prices_stocks = closing_bars()
    sum_closing_prices= closing_prices_stocks['close'].iloc[-3:].sum()
    daily_average = sum_closing_prices/3
    return daily_average    

def stocks_last_hours_close():
    current_price_stocks = hourly_close_bars()
    return float(current_price_stocks)

def stocks_trade_criteria():
    last_five = float(stocks_last_fiveday_avg_close())
    last_hour = float(stocks_last_hours_close())
    difference = last_hour - last_five
    if last_five < last_hour and difference <= 2.00:
        return True
    else:
        return False

