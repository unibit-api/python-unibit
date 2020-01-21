from .unibit import UniBit as ub


class Coverage(ub):

    def getAssetCoverage(self, exchange, datatype="json"):
        endpoints = 'ref/companyList'

        return self.make_request(endpoints=endpoints, data={'exchange': exchange, 'datatype': datatype})

    def getCryptoCoverage(self, datatype="json"):
        endpoints = 'ref/cryptoList'

        return self.make_request(endpoints=endpoints, data={'datatype': datatype})
