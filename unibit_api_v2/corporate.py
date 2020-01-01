from .unibit import UniBit as ub


class Corporate(ub):

    def getCorporateSplits(self, ticker, startDate, endDate, selectedFields="all", datatype='json', size=None):

        if isinstance(ticker, list):
            temp = "";
            for item in ticker:
                temp = temp + item + ","
            ticker = temp

        endpoints = 'company/actions/splits'

        return self.make_request(endpoints=endpoints,
                                 data={'tickers': ticker, 'startDate': startDate, 'endDate': endDate,
                                       'datatype': datatype, 'size': size})

    def getCorporateDividends(self, ticker, startDate, endDate, selectedFields="all", datatype='json', size=None):

        if isinstance(ticker, list):
            temp = "";
            for item in ticker:
                temp = temp + item + ","
            ticker = temp

        endpoints = 'company/actions/dividends'

        return self.make_request(endpoints=endpoints,
                                 data={'tickers': ticker, 'startDate': startDate, 'endDate': endDate,
                                       'datatype': datatype, 'size': size})
