from databuri.datasources import Air4Thai

client = Air4Thai()

params = dict(
    # สถานีจุดวัด กรมประชาสัมพันธ์
    stations=['59t'],
    measurements=['PM25'],
    sdate='2019-08-01', edate='2019-08-05'
)

res = client.fetch(**params)

for r in res:
    print("{DATETIMEDATA} at Station {stationID} | PM25={PM25}".format(**r))
