# UniBit

[![PyPI version](https://badge.fury.io/py/python-unibit.svg)](https://badge.fury.io/py/python-unibit)
[![Documentation Status](https://readthedocs.org/projects/unibit/badge/?version=latest)](https://unibit.readthedocs.io/en/latest/?badge=latest)

*A Python module to get stock data and news from the UniBit API*

UniBit is a free API that provides real time and historical financial data, as well as financial news. This SDK is a client-side implementation of the UniBit API (https://www.unibit.ai) which has Python functions for each available API call. For the UniBit API documentation, visit (https://unibit.ai/docs)

To get started, sign up at (https://unibit.ai/signup) to request a free access key. With a free key, all non-news API features are available with generous rate limits.

The UniBit Stock News API requires a premium account, but in return gives a wealth of news articles on all 8000 US-listed companies. Along with this, UniBit provides analyses on each news article. With deep learning, each article is classified into a comprehensive genre list, and named entities and sentiment are also extracted. 

## Update
Unibit python SDK is now available for Version2 APIs!
For the API documentation, visit (https://unibit.ai/docs/V2.0/introduction)
For the python SDK for Version2 APIs, go to [Version2 APIs example](#version2-apis-examples)
<br />*If there are multiple tickers in your input, please put them into a list, see examples [Version2 APIs example](#version2-apis-examples)*

## Install
To install UniBit, type:
```shell
pip install python-unibit
```

To install from the source, type:
```shell
git clone https://github.com/unibit-api/python-unibit.git
pip install -e python-unibit
```

### API V2.0 Example

Get the real time price of Apple (AAPL)

```python
from unibit_api_v2.stock import StockPrice
sp = StockPrice(key="YOUR_KEY")
aapl_stock = sp.getHistoricalStockPrice(ticker=["AAPL","WORK"],startDate="2019-09-15",endDate="2019-09-20")
```

Get Apple's Company Profile

```python
from unibit_api_v2.company import CompanyInfo
ci = CompanyInfo(key="YOUR_KEY")
aapl_profile = ci.getCompanyProfile(ticker=["AAPL"])
```

Get Apple's Stock News

```python
from unibit_api_v2.news import StockNews
sn = StockNews(key = "YOUR_KEY")
aapl_news = sn.getStockNews(ticker = ["AAPL"], startDate = "2019-08-25", endDate = "2019-08-30", startMinute = "10:00:00", endMinute = "11:00:00", genre = "partnership", sector = "technology")
```

Get Corporate Splits

```python
from unibit_api_v2.corporate import Corporate
corporate = Corporate(key = "YOUR_KEY")
corporate_splits = corporate.getCorporateSplits(ticker = ["all"], startDate="2019-02-01", endDate="2019-02-11")
```

Get Historical Crypto Price

```python
from unibit_api_v2.crypto import CryptoPrice
cp = CryptoPrice(key = "YOUR_KEY")
historical_crypto_price = cp.getHistoricalCryptoPrice(ticker=["BCH-USD"], startDate = "2019-08-25", endDate = "2019-08-30")
```

Get Forex Rate

```python
from unibit_api_v2.forex import ForexRate
fr = ForexRate(key = "YOUR_KEY")
realtime_forex = fr.getRealtimeForexRates(base = "usd", foreign = ["cny","eur","inr"], amount = 1, startDate = "2019-08-29", endDate = "2019-08-29", startMinute = "11:00:00", endMinute = "12:00:00")
```

Get Asset Coverage

```python
from unibit_api_v2.reference import Coverage
c = Coverage(key = "YOUR_KEY")
asset_coverage = c.getAssetCoverage(exchange = "NASDAQ")
```


The CSV format is supported on many of the UniBit APIs. Requesting a CSV datatype will return a ```csv.reader()``` of the data

```python
from unibit.stockprice import StockPrice
sp = StockPrice(key="YOUR_KEY")
aapl_price_csv = sp.getPricesRealTime("AAPL", size=10, datatype="csv")
```

## API V1.0 Example

Get the real time price of Apple (AAPL)

```python
from unibit_api_v1.stockprice import StockPrice
sp = StockPrice(key="YOUR_KEY")
aapl_price = sp.getPricesRealTime("AAPL")
```

Get Apple's Company Profile

```python
from unibit_api_v1.companyinfo import CompanyInfo
ci = CompanyInfo(key="YOUR_KEY")
aapl_profile = ci.getCompanyProfile("AAPL")
```

Get the latest news on Apple

```python
from unibit_api_v1.news import StockNews
sn = StockNews(key="YOUR_KEY")
aapl_news = sn.getLatestStockNews("AAPL")
```

## Contribute!
In the UniBit Python SDK, we not only want to wrap the UniBit API, but open source methods of stock analysis, be it with some fancy quantitative strategy, with graphing, or with machine learning. Propose something in an issue or contact me at stefan@unibit.ai if you want to help!

## Documentation
Detailed documentation on the UniBit API is available at https://unibit.ai/docs/V2.0/introduction

## License
This project is developed under an MIT License. 

