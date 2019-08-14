import requests
from databuri import configuration, logger

# @todo #1 sphink document

"""GovSpending
desc
- param x: ..
- ..
"""
class GovSpending(object):
    """ Set  params (internal used only) """
    URL = 'https://govspendingapi.data.go.th/api/service/cgdcontract'
    LOGGER = logger.getLogger(__name__)
    _L = LOGGER

    def __init__(self, max_retries=5, ipp=50, token=None):
        self.max_retries = max_retries
        self.ipp = ipp

        if not token:
            config = configuration.read_config()
            token = config.get('govspending', 'user_token')

        self.token = token

    def fetch(self, params, attempt=0):
        if not 'offset' in params:
            params['offset'] = 0 

        xparams, _ = self._build_request(params)

        GovSpending._L.info("Sending request to {}".format(GovSpending.URL))
        req = requests.get(GovSpending.URL, xparams)

        if req.status_code in [504, 500]:
            if attempt < self.max_retries:
                attempt = attempt + 1
                print("Retry attempt {} for {}".format(attempt, params))
                return self.fetch(params, attempt=attempt)
            else:
                raise SystemError(
                    "Retries exceeds {} times".format(self.max_retries)
                )
        elif req.status_code == 403:
            raise ValueError(req.text)
        elif req.status_code != 200:
            raise SystemError(
                "code={}".format(req.status_code),
                req.text
            )

        data = req.json()['result']

        if len(data) == self.ipp:
            nextPageParams = dict(**params)
            nextPageParams['offset'] += self.ipp

        return data, nextPageParams

    def _build_request(self, params, headers=[]) -> tuple:
        params = dict(
            user_token=self.token,
            limit=self.ipp,
            **params
        )

        return params, headers
