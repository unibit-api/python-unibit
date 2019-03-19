from .unibit import UniBit as ub

class StockPrice(ub):

	def getPricesRealTime(self, ticker):
		""" Get real time stock prices

		Keyword Arguments:
			ticker: Company ticker 
		"""

		endpoints = ['realtimestock']
		return self.make_request(endpoints=endpoints, ticker=ticker, data={})

	def getPricesHistorical(self, ticker, date_range, interval):
		""" Get real time stock prices

		Keyword Arguments:
			ticker: Company ticker 
			date_range: Range to grab historical prices,
							either 1m, 3m, 1y, 3y, 5y, 10y, or 20y
			interval: A positive number (n). If passed, chart data will 
						return every nth element as defined by Interval
		"""

		if date_range not in ['1m', '3m', '1y', '3y', '5y', '10y', '20y']:
			raise ValueError('Unsupported range value')

		if (not isinstance(interval, int) or interval <= 0):
			raise ValueError('Interval must be a positive integer')

		endpoints = ['historicalstockprice']

		return self.make_request(endpoints=endpoints, ticker=ticker, data={'range':date_range, 'interval':interval})



		
