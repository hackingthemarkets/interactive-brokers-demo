from ib_insync import *

ib = IB()
ib.connect('127.0.0.1', 7497, clientId=1)

allParams = ib.reqScannerParameters()
print(allParams)

subscription = ScannerSubscription(instrument='STK', locationCode='STK.US.MAJOR', scanCode='SCAN_currYrETFFYDividendYield_DESC')

scanData = ib.reqScannerData(subscription)

for scan in scanData:
    #print(scan)
    print(scan.contractDetails.contract.symbol)
    
