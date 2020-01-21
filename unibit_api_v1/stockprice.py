from .unibit import UniBit as ub


class StockPrice(ub):

    def getPricesRealTime(self, ticker, size=None, datatype='json'):
        """ Get real time stock prices

        Keyword Arguments:
            ticker: Company ticker
            datatype: Data type of response. Either 'json' or 'csv'
            size: Integer (n) which will have the response return the latest n prices.
                    If unspecified, all real time results will be returned, going back 1 month.
        """

        endpoints = ['realtimestock']
        return self.make_request(endpoints=endpoints, ticker=ticker, data={'datatype': datatype, 'size': size})

    def getPricesHistorical(self, ticker, range, interval, datatype='json'):
        """ Get real time stock prices

        Keyword Arguments:
            ticker: Company ticker
            date_range: Range to grab historical prices,
                            either 1m, 3m, 1y, 3y, 5y, 10y, or 20y
            interval: A positive number (n). If passed, chart data will
                        return every nth element as defined by Interval
            datatype: Data type of response. Either 'json' or 'csv'
        """

        if range not in ['1m', '3m', '1y', '3y', '5y', '10y', '20y']:
            raise ValueError('Unsupported range value')

        if (not isinstance(interval, int) or interval <= 0):
            raise ValueError('Interval must be a positive integer')

        endpoints = ['historicalstockprice']

        return self.make_request(endpoints=endpoints, ticker=ticker,
                                 data={'range': range, 'interval': interval, 'datatype': datatype})
