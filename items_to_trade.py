from api_info import Api


class Stocks_to_be_traded(Api):
    """Stocks that are being traded"""
    pass      

twr = Stocks_to_be_traded("Twitter",'TWTR')
tsl = Stocks_to_be_traded("Tesla","TSLA")

actual_stocks = [twr,tsl]

class Cryptos_to_be_traded(Api):
    """Crypto currency that are being traded"""
    pass

bit = Cryptos_to_be_traded('bitcoin', 'BTCUSD')
ethereum = Cryptos_to_be_traded('ethereum','ETHUSD')

actual_cryptos= [bit,ethereum]