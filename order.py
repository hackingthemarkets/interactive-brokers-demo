from ib_insync import *

ib = IB()
ib.connect('127.0.0.1', 7497, clientId=1)

stock = Stock('AAPL', 'SMART', 'USD')

order = MarketOrder('BUY', 10)

trade = ib.placeOrder(stock, order)

print(trade)

def orderFilled(trade, fill):
    print("order has been filled")
    print(trade)
    print(fill)

trade.fillEvent += orderFilled

ib.sleep(3)

for trade in ib.trades():
    print("== this is one of my trades =")
    print(trade)

for order in ib.orders():
    print("== this is one of my orders ==")
    print(order)

ib.run()