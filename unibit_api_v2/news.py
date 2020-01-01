from .unibit import UniBit as ub

class StockNews(ub):

	def getStockNews(self, ticker, startDate, endDate, startMinute, endMinute, genre, sector, selectedFields = "all", datatype = "json", size = None):
		if isinstance(ticker, list):
			temp = "";
			for item in ticker:
				temp = temp + item + ","
			ticker = temp

		endpoints = 'company/news'

		return self.make_request(endpoints=endpoints, data={'tickers': ticker, 'startDate': startDate, 'endDate': endDate, 'startMinute': startMinute, 'endMinute': endMinute, 'genre': genre, 'sector':sector, 'datatype':datatype ,'size':size})
