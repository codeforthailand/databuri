from databuri.datasources import GovSpending

client = GovSpending()

params = dict(year=2561, keyword="โรงเรียน", offset=0)

projects = client.fetch(params)
print(projects)

for p in projects[:10]:
    print("{project_name}\n มูลค่า {value}".format(
        project_name=p['project_name'],
        value=p['sum_price_agree']
    ))
