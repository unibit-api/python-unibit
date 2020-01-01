from .unibit import UniBit as ub


class CompanyInfo(ub):

    def getCompanyFinancials(self, ticker, financial_type, interval, datatype='json'):
        """ Get company financials by ticker

        Keyword Arguments:
            ticker: Company ticker
            financial_type: Type of company financial to access, either
                                'income_statement', 'balance_sheet' or 'cash_flow'
            interval: Interval of company financial, either 'annual' or 'quarterly'
            datatype: Data type of response. Either 'json' or 'csv'
        """

        if financial_type not in ['income_statement', 'balance_sheet', 'cash_flow']:
            raise ValueError('Unsupported Financial Type value')

        if interval not in ['annual', 'quarterly']:
            raise ValueError('Unsupported Interval value')

        endpoints = ['financials']

        return self.make_request(ticker=ticker, endpoints=endpoints,
                                 data={'type': financial_type, 'interval': interval, 'datatype': datatype})

    def getCompanyProfile(self, ticker, datatype='json'):
        """ Get company profile by ticker

        Keyword Arguments:
            ticker: Company ticker
            datatype: Data type of response. Either 'json' or 'csv'
        """

        endpoints = ['companyprofile']
        return self.make_request(ticker=ticker, endpoints=endpoints, data={'datatype': datatype})

    def getCompanyFinancialSummary(self, ticker, datatype='json'):
        """ Get company financial summary by ticker

        Keyword Arguments:
            ticker: Company ticker
            datatype: Data type of response. Either 'json' or 'csv'
        """

        endpoints = ['financials', 'summary']
        return self.make_request(ticker=ticker, endpoints=endpoints, data={'datatype': datatype})

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

        return self.make_request(ticker=ticker, endpoints=endpoints, data={'ownership_type': ownership_type})

    def getInsiderTransactions(self, ticker, datatype='json', size=None):
        """ Get insider transactions by ticker

        Keyword Arguments:
            ticker: Company ticker
            datatype: Data type of response. Either 'json' or 'csv'
        """

        endpoints = ['insidertrading']

        return self.make_request(ticker=ticker, endpoints=endpoints, data={'datatype': datatype, 'size': size})

    def getCIKNumber(self, ticker):
        """ Get CIK Number by ticker

        Keyword Arguments:
            ticker: Company ticker
        """
        endpoints = ['company', 'cik']

        return self.make_request(ticker=ticker, endpoints=endpoints, data={})

    def getSECFilingLinks(self, ticker, datatype='json'):
        """ Get SEC Filing links by ticker

        Keyword Arguments:
            ticker: Company ticker
            datatype: Data type of response. Either 'json' or 'csv'
        """
        endpoints = ['company', 'sec']

        return self.make_request(ticker=ticker, endpoints=endpoints, data={'datatype': datatype})
