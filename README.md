# UniBit

[![PyPI version](https://badge.fury.io/py/python-unibit.svg)](https://badge.fury.io/py/python-unibit)
[![Documentation Status](https://readthedocs.org/projects/unibit/badge/?version=latest)](https://unibit.readthedocs.io/en/latest/?badge=latest)

*A Python module to get stock data and news from the UniBit API*

UniBit is a free API that provides real time and historical financial data, as well as financial news. This SDK is a client-side implementation of the UniBit API (https://www.unibit.ai) which has Python functions for each available API call. For the UniBit API documentation, visit (https://unibit.ai/docs)

To get started, sign up at (https://unibit.ai/login) to request a free access key. With a free key, all non-news API features are available with generous rate limits.

The UniBit Stock News API requires a premium account, but in return gives a wealth of news articles on all 8000 US-listed companies. Along with this, UniBit provides analyses on each news article. With deep learning, each article is classified into a comprehensive genre list, and named entities and sentiment are also extracted. 

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

## Examples

Get the real time price of Apple (AAPL)

```python
from unibit.stockprice import StockPrice
sp = StockPrice(key="YOUR_KEY")
aapl_price = sp.getPricesRealTime("AAPL")
```

Get Apple's Company Profile

```python
from unibit.companyinfo import CompanyInfo
ci = CompanyInfo(key="YOUR_KEY")
aapl_profile = ci.getCompanyProfile("AAPL")
```

Get the latest news on Apple

```python
from unibit.news import StockNews
sn = StockNews(key="YOUR_KEY")
aapl_news = sn.getLatestStockNews("AAPL")
```

The CSV format is supported on many of the UniBit APIs. Requesting a CSV datatype will return a ```csv.reader()``` of the data

```python
from unibit.stockprice import StockPrice
sp = StockPrice(key="YOUR_KEY")
aapl_price_csv = sp.getPricesRealTime("AAPL", size=10, datatype="csv")
```

## Contribute!
In the UniBit Python SDK, we not only want to wrap the UniBit API, but open source methods of stock analysis, be it with some fancy quantitative strategy, with graphing, or with machine learning. Propose something in an issue or contact me at stefan@unibit.ai if you want to help!

## Documentation
Detailed documentation on the UniBit API is available at https://unibit.ai/docs.

## License
This project is developed under an MIT License. 

