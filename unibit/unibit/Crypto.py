from .unibit import UniBit as ub

class Crypto(ub):

   def getHistoricalCryptoPrice(self, ticker, range, interval, datatype='json'):


       if range not in ['1m', '3m', '1y', '3y', '5y', '10y']:
           raise ValueError('Unsupported range value')

       if (not isinstance(interval, int) or interval <= 0):
           raise ValueError('Interval must be a positive integer')

       endpoints = ['historicalcryptoprice']

       return self.make_request(endpoints=endpoints, ticker=ticker,
                                data={'range': range, 'interval': interval, 'datatype': datatype})