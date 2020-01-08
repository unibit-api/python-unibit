from .unibit import UniBit as ub


class CryptoPrice(ub):

    def getHistoricalCryptoPrice(self, ticker, startDate, endDate, size=None, selectedFields="all", datatype="json"):

        if isinstance(ticker, list):
            ticker = ",".join(ticker)

        endpoints = 'crypto/historical'

        return self.make_request(endpoints=endpoints,
                                 data={'tickers': ticker, 'startDate': startDate, 'endDate': endDate,
                                       'datatype': datatype, 'size': size})
