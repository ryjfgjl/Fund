# http://fund.eastmoney.com/Data/FundDataPortfolio_Interface.aspx?dt=14&mc=returnjson&ft=all&pn=500&pi=200&sc=abbname&st=asc
# 基金经理

import requests
from sql import Sql
from datetime import date


Sql = Sql()
db_conn = Sql.conn_db('fund')


url = 'http://fund.eastmoney.com/Data/FundDataPortfolio_Interface.aspx?dt=14&mc=returnjson&ft=all&pn=50&pi=1&sc=abbname&st=asc'
response = requests.get(url)
html = response.text
data = html[len('var returnjson= {data:[['):(len(html.split(']')[-1])+2)*-1]
managers = data.split('],[')
pages = int(html.split(']')[-1].split('pages:')[-1].split(',')[0])

for page in range(pages):
    page+=1
    url = 'http://fund.eastmoney.com/Data/FundDataPortfolio_Interface.aspx?dt=14&mc=returnjson&ft=all&pn={}&pi={}&sc=abbname&st=asc'.format(pages,page)
    response = requests.get(url)
    html = response.text
    data = html[len('var returnjson= {data:[['):(len(html.split(']')[-1]) + 2) * -1]
    managers = data.split('],[')
    for manager in managers:
        manager = manager[1:-1].split('","')

        code = manager[0]
        name = manager[1]
        companycode = manager[2]
        companyname = manager[3]
        currentfundcodes = manager[4]
        currentfundnames = manager[5]
        managertotalday = manager[6]
        bestincomerate = manager[7]
        bestfundcode = manager[8]
        bestfundname = manager[9]
        bestfundmoney = manager[10]
        bestfundincomerate = manager[11]
        crawldate = str(date.today())

        sql = "insert into manager(code,name,companycode,companyname,currentfundcodes,currentfundnames,managertotalday,bestincomerate,bestfundcode,bestfundname,bestfundmoney,bestfundincomerate," \
              "crawldate) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        Sql.exec_sql(db_conn, sql, [[code,name,companycode,companyname,currentfundcodes,currentfundnames,managertotalday,bestincomerate,bestfundcode,bestfundname,bestfundmoney,bestfundincomerate,crawldate]])











