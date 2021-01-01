from ib_insync import *
from bs4 import BeautifulSoup as bs

ib = IB()
ib.connect('127.0.0.1', 7497, clientId=1)

stock = Stock('AAPL', 'SMART', 'USD')

# * 'ReportsFinSummary': Financial summary
# * 'ReportsOwnership': Company's ownership
# * 'ReportSnapshot': Company's financial overview
# * 'ReportsFinStatements': Financial Statements
# * 'RESC': Analyst Estimates
# * 'CalendarReport': Company's calendar

fundamentals = ib.reqFundamentalData(stock, 'ReportSnapshot')

print(fundamentals)

content = bs(fundamentals, "xml")

ratios = content.find_all("Ratio")

for ratio in ratios:
    print(ratio['FieldName'])
    print(ratio.text)