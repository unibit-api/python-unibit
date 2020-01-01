from .unibit import UniBit as ub


class CompanyInfo(ub):

    def getCompanyFinancials(self, ticker, interval, statement, startDate, endDate, selectedFields="all",
                             datatype='json'):
        """ Get company financials by ticker
        Keyword Arguments:
            ticker: Company ticker
            financial_type: Type of company financial to access, either
                                'income_statement', 'balance_sheet' or 'cash_flow'
            interval: Interval of company financial, either 'annual' or 'quarterly'
            datatype: Data type of response. Either 'json' or 'csv'
        """

        if statement not in ['income_statement', 'balance_sheet', 'cash_flow', 'all']:
            raise ValueError('Unsupported Financial Type value')

        if interval not in ['annual', 'quarterly']:
            raise ValueError('Unsupported Interval value')

        if isinstance(ticker, list):
            temp = "";
            for item in ticker:
                temp = temp + item + ","
            ticker = temp

        endpoints = 'company/financials'

        return self.make_request(endpoints=endpoints,
                                 data={'tickers': ticker, 'statement': statement, 'startDate': startDate,
                                       'endDate': endDate, 'interval': interval, 'datatype': datatype})

    def getCompanyProfile(self, ticker, selectedFields="all", datatype='json'):
        """ Get company profile by ticker
        Keyword Arguments:
            ticker: Company ticker
            datatype: Data type of response. Either 'json' or 'csv'
        """

        if isinstance(ticker, list):
            temp = "";
            for item in ticker:
                temp = temp + item + ","
            ticker = temp

        endpoints = 'company/profile'

        return self.make_request(endpoints=endpoints, data={'tickers': ticker, 'datatype': datatype})

    def getCompanyFinancialSummary(self, ticker, selectedFields="all", datatype='json'):
        """ Get company financial summary by ticker
        Keyword Arguments:
            ticker: Company ticker
            datatype: Data type of response. Either 'json' or 'csv'
        """
        if isinstance(ticker, list):
            temp = "";
            for item in ticker:
                temp = temp + item + ","
            ticker = temp

        endpoints = 'company/financialSummary'
        return self.make_request(endpoints=endpoints, data={'tickers': ticker, 'datatype': datatype})

    def getOwnershipStructure(self, ticker, ownershipType, startDate, endDate, selectedFields="all", datatype="json"):
        """ Get company ownership structure
        Keyword Arguments:
            ticker: Company ticker
            ownership_type: Ownership Type, either
                                'majority_holder', 'top_institutional_holder', or 'top_mutual_fund_holder'
        """
        if isinstance(ticker, list):
            temp = "";
            for item in ticker:
                temp = temp + item + ","
            ticker = temp

        if ownershipType not in ['majority_holder', 'top_institutional_holder', 'top_mutual_fund_holder']:
            raise ValueError('Unsupported Ownership Type')

        endpoints = 'company/ownership'

        return self.make_request(endpoints=endpoints,
                                 data={'tickers': ticker, 'ownershipType': ownershipType, 'startDate': startDate,
                                       'endDate': endDate, 'datatype': datatype})

    def getInsiderTransactions(self, ticker, startDate, endDate, selectedFields="all", datatype='json', size=None):
        """ Get insider transactions by ticker
        Keyword Arguments:
            ticker: Company ticker
            datatype: Data type of response. Either 'json' or 'csv'
        """
        if isinstance(ticker, list):
            temp = "";
            for item in ticker:
                temp = temp + item + ","
            ticker = temp

        endpoints = 'company/insiderTransaction'

        return self.make_request(endpoints=endpoints,
                                 data={'tickers': ticker, 'startDate': startDate, 'endDate': endDate,
                                       'datatype': datatype, 'size': size})

    # def getCIKNumber(self, ticker):
    # 	""" Get CIK Number by ticker
    # 	Keyword Arguments:
    # 		ticker: Company ticker
    # 	"""
    # 	endpoints = ['company', 'cik']

    # 	return self.make_request(ticker=ticker, endpoints=endpoints, data={})

    def getSECFilingLinks(self, ticker, startDate, endDate, selectedFields="all", datatype='json', size=None):
        """ Get SEC Filing links by ticker
        Keyword Arguments:
            ticker: Company ticker
            datatype: Data type of response. Either 'json' or 'csv'
        """
        if isinstance(ticker, list):
            temp = "";
            for item in ticker:
                temp = temp + item + ","
            ticker = temp

        endpoints = 'company/secFilingLink'

        return self.make_request(endpoints=endpoints,
                                 data={'tickers': ticker, 'startDate': startDate, 'endDate': endDate,
                                       'datatype': datatype, 'size': size})
