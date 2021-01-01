from ib_insync import *

ib = IB()

# use this instead for IB Gateway
# ib.connect('127.0.0.1', 7497, clientId=1)

# us this for TWS (Workstation)
ib.connect('127.0.0.1', 7497, clientId=1)

stock = Stock('AMD', 'SMART', 'USD')

bars = ib.reqHistoricalData(
    stock, endDateTime='', durationStr='30 D',
    barSizeSetting='1 hour', whatToShow='MIDPOINT', useRTH=True)

# convert to pandas dataframe
df = util.df(bars)
print(df)

market_data = ib.reqMktData(stock, '', False, False)

def onPendingTicker(ticker):
    print("pending ticker event received")
    print(ticker)

ib.pendingTickersEvent += onPendingTicker

ib.run()