from ib_insync import *

ib = IB()
ib.connect('127.0.0.1', 7497, clientId=1)

stock = Stock('AAPL', 'SMART', 'USD')
ib.qualifyContracts(stock)

ib.sleep(1)

chains = ib.reqSecDefOptParams(stock.symbol, '', stock.secType, stock.conId)

print(util.df(chains))