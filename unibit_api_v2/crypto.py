from .unibit import UniBit as ub


class CryptoPrice(ub):

    def getHistoricalCryptoPrice(self, ticker, startDate, endDate, size=None, selectedFields="all", datatype="json"):

        if isinstance(ticker, list):
            temp = "";
            for item in ticker:
                temp = temp + item + ","
            ticker = temp

        endpoints = 'crypto/historical'

        return self.make_request(endpoints=endpoints,
                                 data={'tickers': ticker, 'startDate': startDate, 'endDate': endDate,
                                       'datatype': datatype, 'size': size})
