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

num_box = num_boxes[0]

lies = num_box.xpath('//div/ul/li[1]')[0]
print(lies)
fund = lies.xpath('//li/div/a[1]/text()')[0]
print(fund)

"""
for num_box in [num_boxes[0]]:    lies = num_box.xpath('//div[@id="code_content"]//div[@class="num_box"]/ul/li')
    lies = num_box.xpath('//div[@id="code_content"]//div[@class="num_box"]/ul/li')
    for li in [lies[0]]:
        fund = li.xpath('//div[@id="code_content"]//div[@class="num_box"]/ul/li/div/a[1]/text()')
        code = fund[0].strip('(')
        #name = fund[1].strip()
        #allfund.append([code, name])
#sql = 'insert into fund(code, name) select "{0}", "{1}"'.format(code, name)
#Sql.exec_sq(db_conn, sql, allfund)
        
"""
