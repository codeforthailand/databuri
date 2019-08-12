import requests
from databuri import configuration

"""GovSpending
desc
- param x: ..
- ..
"""


class GovSpending(object):
    """ Set  params (internal used only) """
    URL = 'https://govspendingapi.data.go.th/api/service/cgdcontract'

    def __init__(self, max_retries=5, limit=50):
        print("LIMIT %d" % limit)

        self.max_retries = max_retries
        self.limit = limit

        config = configuration.read_config()
        self.token = config.get('govspending', 'user_token')

    def fetch(self, params, attempt=0):
        params, _ = self._build_request(params)
        print(params)

        # @todo #1 add logging

        req = requests.get(GovSpending.URL, params)
        print(req)

        data = req.json()['result']

        return data

    def _build_request(self, params, headers=[]) -> tuple:
        params = dict(
            user_token=self.token,
            **params
        )

        return params, headers
