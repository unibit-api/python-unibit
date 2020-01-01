from .unibit import UniBit as ub


class StockNews(ub):

    def getLatestStockNews(self, ticker, datatype='json'):
        """ Get latest stock news by ticker

        Keyword Arguments:
            ticker: Company ticker
            datatype: Data type of response. Either 'json' or 'csv'
        """

        endpoints = ['news', 'latest']

        return self.make_request(ticker=ticker, endpoints=endpoints, data={'datatype': datatype})

    def getStockNewsAnalysis(self, ticker, range):
        """ Get analyzed stock news, including tags, sentiment, and named entities

        Keyword Arguments:
            ticker: Company ticker
            interval: Either "realtime", "1w", "1m", or "3m"
        """

        endpoints = ['news', 'sentiment']

        if range not in ['realtime', '1w', '1m', '3m']:
            raise ValueError('Unsupported Interval value')

        return self.make_request(ticker=ticker, endpoints=endpoints, data={'range': range})

    def getStockNewsByClassification(self, ticker, event_genre, event_sector, range):

        endpoints = ['classification']

        if event_genre not in ['M&A', 'partnership', 'credit market', 'expansion', 'fundingxx', 'funding',
                               'analyst estimate', 'data leak', 'product release',
                               'regulatory', 'blackchain', 'fraud', 'lawsuit', 'charity', 'education', 'philanthropy',
                               'retail', 'analyst rating', 'backruptcy', 'international affairs',
                               'cyber security', 'antitrust', 'corruption', 'tariff', 'environment', 'earnings',
                               'labor market', 'fixed income', 'food', 'commodities', 'media', 'climate change',
                               'startup', 'autonomous car', 'achievement', 'corporate leadership', 'investment',
                               'pharmaceutical', 'energy market', 'equities', 'financing', 'valuation',
                               'intellectual property',
                               'currencies', 'market performance', 'taxation', 'economic data', 'cloud computing',
                               'trade', 'central bank', 'product', 'automotive', 'machine learning', 'recession',
                               'emerging market', 'technical analysis']:
            raise ValueError('Unsupported Financial Type value')

        if event_sector not in ['healthcare', 'energy', 'basic materials', 'industrials', 'technology',
                                'financial services', 'communication services', 'consumer cyclical',
                                'consumer defensive', 'utilities', 'real estate']:
            raise ValueError('Unsupported Financial Type value')

        if range not in ['realtime', '1w', '1m', '3m']:
            raise ValueError('Unsupported Financial Type value')

        endpoints = ['classification']

        return self.make_request(ticker=ticker, endpoints=endpoints,
                                 data={'range': range, 'event_genre': event_genre, 'event_sector': event_sector})
