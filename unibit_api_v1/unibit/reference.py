from .unibit import UniBit as ub


class Reference(ub):

    def getAssetCoverage(self, exchange, datatype='json'):
        """ Get latest stock news by ticker

        Keyword Arguments:
            ticker: Company ticker
            datatype: Data type of response. Either 'json' or 'csv'
        """

        endpoints = ['companylist']

        return self.make_request(endpoints=endpoints, ticker="", data={'datatype': datatype, "exchange": exchange})
