import requests

from datetime import datetime

_API_TEMPLATE = 'http://air4thai.pcd.go.th/webV2/history/api/data.php?stationID={station_ids}' + \
                '&param={measurements}&type=hr&sdate={sdate}&edate={edate}' + \
                '&stime=00&etime=24'

_STATIC_COLS = ['stationID', 'DATETIMEDATA']


class Air4Thai(object):
    def fetch(
        self,
        stations=[],
        measurements=[],
        sdate='2019-01-01',
        edate=datetime.now().strftime('%Y-%m-%d'),
    ):

        url = _API_TEMPLATE.format(
            station_ids=','.join(stations),
            measurements=','.join(measurements),
            sdate=sdate,
            edate=edate
        )

        res = requests.get(url)

        data = res.json()

        records = []

        for s in data['stations']:
            for r in s['data']:
                records.append(dict(stationID=s['stationID'], **r))

        return records
