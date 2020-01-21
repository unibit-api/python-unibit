from unibit.Crypto import Crypto
from unibit.Forex import Forex
from unibit.companyinfo import CompanyInfo
from unibit.news import StockNews
from unibit.reference import Reference
from unibit.stockprice import StockPrice

rf = Reference(key="demo")
data1 = rf.getAssetCoverage(exchange="ASX")
print(data1)

stock = StockPrice(key="demo")
data2 = stock.getPricesRealTime(ticker="AAPL", size=10)
print(data2)

data3 = stock.getPricesHistorical(ticker="AAPL", range="1m", interval=1)
print(data3)

companyInfo = CompanyInfo(key="demo")
data4 = companyInfo.getCIKNumber("AAPL")
print(data4)

data5 = companyInfo.getCompanyFinancials(ticker="AAPL", financial_type="cash_flow", interval="annual")
print(data5)

data6 = companyInfo.getCompanyProfile(ticker="AAPL")
print(data6)

data7 = companyInfo.getCompanyFinancialSummary(ticker="AAPL")
print(data7)

data8 = companyInfo.getOwnershipStructure(ticker="AAPL", ownership_type="majority_holder")
print(data8)

data9 = companyInfo.getInsiderTransactions(ticker="AAPL", size=5)
print(data9)

data10 = companyInfo.getSECFilingLinks(ticker="AAPL")
print(data10)

# need to figure it out have some bugs
news = StockNews(key="demo")
data11 = news.getLatestStockNews(ticker="AAPL")
print(data11)

data12 = news.getStockNewsAnalysis(ticker="AAPL", range="1w")
print(data12)

forex = Forex(key="NVhnTCzYzE-RbioZOpvYCxhTOgwVRl3M")
data13 = forex.getForex(base_Currency="USD", currency="CNY,EUR", size=1, amount=10)
print(data13)

crypto = Crypto(key="NVhnTCzYzE-RbioZOpvYCxhTOgwVRl3M")
data14 = crypto.getHistoricalCryptoPrice(ticker="BTC", range="3m", interval=1)
print(data14)
