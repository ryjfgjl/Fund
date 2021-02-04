# http://fund.eastmoney.com/Company/default.html#scomname;dasc
# 基金公司

import requests
from sql import Sql
from datetime import date
from bs4 import BeautifulSoup

Sql = Sql()
db_conn = Sql.conn_db('fund')


url = 'http://fund.eastmoney.com/Company/default.html#scomname;dasc'
response = requests.get(url)
response.encoding = 'utf8'
html = response.text
soup = BeautifulSoup(html, 'html.parser')
trs = soup.find('table', id='gspmTbl').find('tbody').find_all('tr')


for tr in trs:
    tds = tr.find_all('td')
    code = tds[1].find('a')['href']
    name = tds[1].get_text()
    establishdate = tds[3].get_text()
    lables = tds[4].find_all('label', 'sprite sprite-star1')
    txscore = len(lables)
    scalenumber = tds[5]['data-sortvalue']
    allfundnumber = tds[6].get_text()
    allmanagernumber = tds[7].get_text()
    crawldate = str(date.today())

    sql = "insert into company (code,name,establishdate,txscore,scalenumber,allfundnumber,allmanagernumber,crawldate) values(%s,%s,%s,%s,%s,%s,%s,%s)"
    Sql.exec_sql(db_conn, sql, [[code,name,establishdate,txscore,scalenumber,allfundnumber,allmanagernumber,crawldate]])











