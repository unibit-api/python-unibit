from .unibit import UniBit as ub


class StockNews(ub):

    def getStockNews(self, ticker, startDate, endDate, startMinute, endMinute, genre, sector, selectedFields=None,
                     datatype="json", size=None):
        if isinstance(ticker, list):
            ticker = ",".join(ticker)
        else:
            raise TypeError('ticker input should be a list')

        endpoints = 'company/news'

        return self.make_request(endpoints=endpoints,
                                 data={'tickers': ticker, 'startDate': startDate, 'endDate': endDate,
                                       'startMinute': startMinute, 'endMinute': endMinute, 'genre': genre,
                                       'sector': sector, 'datatype': datatype, 'size': size, 'selectedFields': selectedFields})
