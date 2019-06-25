from .unibit import UniBit as ub

class Forex(ub):

    def getForex(self, base_Currency, currency, amount, size, datatype='json'):
        """ Get latest stock news by ticker

        Keyword Arguments:
            ticker: Company ticker
            datatype: Data type of response. Either 'json' or 'csv'
        """

        endpoints = ['forexrealtime']

        return self.make_request(endpoints=endpoints, ticker=base_Currency, data={'datatype': datatype, currency:currency , amount:amount, size:size})
    