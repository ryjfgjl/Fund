# all fund code

import requests
from lxml import etree
from sql import Sql

Sql = Sql()
db_conn = Sql.conn_db('fund')

url = 'http://fund.eastmoney.com/allfund.html'
r = requests.get(url)
r.encoding = 'gb2312'
html = r.text
html = etree.HTML(html)
num_boxes = html.xpath('//div[@id="code_content"]//div[@class="num_box"]')
allfund = []


for num_box in [num_boxes[0]]:
    lies = num_box.xpath('//div[@id="code_content"]//div[@class="num_box"]/ul/li')
    for li in [lies[0]]:
        funds = li.xpath('//div[@id="code_content"]//div[@class="num_box"]/ul/li/div/a[1]/text()')
        for fund in funds:
            print(fund)
            code = fund.split('）')[0][1:]
            name = fund.split('）')[1]
            sql = 'insert into fund(code, name) values ("{}", "{}")'.format(code, name)
            Sql.exec_sql(db_conn, sql)



