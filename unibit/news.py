from .unibit import UniBit as ub

class StockNews(ub):

	def getLatestStockNews(self, ticker):
		""" Get latest stock news by ticker

		Keyword Arguments:
			ticker: Company ticker 
		"""

		endpoints = ['news', 'latest']

		return self.make_request(ticker=ticker, endpoints=endpoints, data={})

	def getStockNewsAnalysis(self, ticker, interval):
		""" Get analyzed stock news, including tags, sentiment, and named entities

		Keyword Arguments:
			ticker: Company ticker 
			interval: Either "realtime", "1w", "1m", or "3m"
		"""

		endpoints = ['news']

		if interval not in ['realtime', '1w', '1m', '3m']:
			raise ValueError('Unsupported Interval value')

		return self.make_request(ticker=ticker, endpoints=endpoints, data={'interval':interval})

