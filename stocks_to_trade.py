from api_call import Api_call


class Stocks_to_be_traded(Api_call):
    """Stocks that are being traded"""
    pass      

twr = Stocks_to_be_traded("Twitter",'TWTR')
tsl = Stocks_to_be_traded("Tesla","TSLA")

actual_stocks = [twr,tsl]

