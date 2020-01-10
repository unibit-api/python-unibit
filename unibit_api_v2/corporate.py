from .unibit import UniBit as ub


class Corporate(ub):

    def getCorporateSplits(self, ticker, startDate, endDate, selectedFields="all", datatype='json', size=None):

        if isinstance(ticker, list):
            ticker = ",".join(ticker)
        else:
            raise TypeError('ticker input should be a list')

        endpoints = 'company/actions/splits'

        return self.make_request(endpoints=endpoints,
                                 data={'tickers': ticker, 'startDate': startDate, 'endDate': endDate,
                                       'datatype': datatype, 'size': size})

    def getCorporateDividends(self, ticker, startDate, endDate, selectedFields="all", datatype='json', size=None):

        if isinstance(ticker, list):
            ticker = ",".join(ticker)
        else:
            raise TypeError('tickers input should be a list')

        endpoints = 'company/actions/dividends'

        return self.make_request(endpoints=endpoints,
                                 data={'tickers': ticker, 'startDate': startDate, 'endDate': endDate,
                                       'datatype': datatype, 'size': size})
