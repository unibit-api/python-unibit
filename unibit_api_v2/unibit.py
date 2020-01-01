import csv

import requests


class UniBit(object):
    _UNIBIT_API_CALL_BASE = "https://api.unibit.ai/v2/"
    _VALID_DATA_TYPE = ['json', 'csv']

    def __init__(self, key):
        """ Initialize the UniBit class
        Keyword Arguments:
            key:  UniBit API key
            nic:  Network Interface
        """

        # Your API Key
        if not isinstance(key, str):
            raise ValueError('API key must be a string')

        self.key = key

    def make_request(self, endpoints, data):
        """ Make a request to the UniBit API
        Keyword Arguments:
            categories: Name of the API call
            symbol: Ticker
            data: Data passed to UniBit API
        """
        url = '{}{}?'.format(self._UNIBIT_API_CALL_BASE, endpoints)
        # print(url);
        data['accessKey'] = self.key

        # Remove all optional keys left unspecified
        for k in list(data):
            if data[k] is None:
                data.pop(k)

        if 'dataType' in data and data['dataType'] not in self._VALID_DATA_TYPE:
            data['dataType'] = 'json'

        return self._handle_request(url, data)

    def _handle_request(self, url, data):
        """ Helper to formally send a request
        Keyword Arguments:
            url: URL to query
            data: API call arguments
        """

        res = requests.get(url, params=data)

        if res.status_code != 200:
            error_response = res.json()
            raise requests.ConnectionError(str(error_response))

        # Handle possibly faulty response
        try:
            if 'dataType' in data and data['dataType'] == 'csv':
                decoded_content = res.content.decode('utf-8')
                response_data = csv.reader(decoded_content.splitlines(), delimiter=',')

            else:
                response_data = res.json()

        except Exception as e:
            print("Received error: {} \n from response value {}".format(e, res))
            response_data = None

        return response_data
