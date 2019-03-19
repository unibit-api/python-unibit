from .unibit import UniBit as ub

class CompanyInfo(ub):

	def getCompanyFinancials(self, ticker, financial_type, interval):
		""" Get company financials by ticker

		Keyword Arguments:
			ticker: Company ticker
			financial_type: Type of company financial to access, either
								'income_statement', 'balance_sheet' or 'cash_flow'
			interval: Interval of company financial, either 'annual' or 'quarterly' 
		"""

		if financial_type not in ['income_statement', 'balance_sheet', 'cash_flow']:
			raise ValueError('Unsupported Financial Type value')

		if interval not in ['annual', 'quarterly']:
			raise ValueError('Unsupported Interval value')

		endpoints = ['financials']

		return self.make_request(ticker=ticker,  endpoints=endpoints, data={'type':financial_type, 'interval':interval})

	def getCompanyProfile(self, ticker):
		""" Get company profile by ticker

		Keyword Arguments:
			ticker: Company ticker 
		"""

		endpoints = ['companyprofile']
		return self.make_request(ticker=ticker, endpoints=endpoints, data={})

	def getCompanyFinancialSummary(self, ticker):
		""" Get company financial summary by ticker

		Keyword Arguments:
			ticker: Company ticker 
		"""

		endpoints = ['financials', 'summary']
		return self.make_request(ticker=ticker, endpoints=endpoints, data={})

	def getOwnershipStructure(self, ticker, ownership_type):
		""" Get company ownership structure

		Keyword Arguments:
			ticker: Company ticker 
			ownership_type: Ownership Type, either
								'majority_holder', 'top_institutional_holder', or 'top_mutual_fund_holder'
		"""

		endpoints = ['ownership']

		if ownership_type not in ['majority_holder', 'top_institutional_holder', 'top_mutual_fund_holder']:
			raise ValueError('Unsupported Ownership Type')

		return self.make_request(ticker=ticker, endpoints=endpoints, data={'ownership_type':ownership_type})

	def getInsiderTransactions(self, ticker):
		""" Get insider transactions by ticker

		Keyword Arguments:
			ticker: Company ticker 
		"""

		endpoints = ['insidertrading']

		return self.make_request(ticker=ticker, endpoints=endpoints, data={})

	def getCIKNumber(self, ticker):
		""" Get CIK Number by ticker

		Keyword Arguments:
			ticker: Company ticker 
		"""
		endpoints = ['company', 'cik']

		return self.make_request(ticker=ticker, endpoints=endpoints, data={})

	def getSECFilingLinks(self,ticker):
		""" Get SEC Filing links by ticker

		Keyword Arguments:
			ticker: Company ticker 
		"""
		endpoints = ['company', 'sec']

		return self.make_request(ticker=ticker, endpoints=endpoints, data={})