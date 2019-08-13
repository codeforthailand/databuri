from databuri.datasources import GovSpending

client = GovSpending()

params = dict(year=2561, keyword="โรงเรียน")

count = 0
while count < 4:
    projects, params = client.fetch(params)
    print("Got %d projects" % (len(projects)))
    print("next page params: ", params)

    for p in projects[:10]:
        print("{project_name}\n มูลค่า {value}".format(
            project_name=p['project_name'],
            value=p['sum_price_agree']
        ))

    count += 1