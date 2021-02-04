
# http://fundf10.eastmoney.com/jbgk_260108.html
# 基金概况
import scrapy
from fund.jjgk_items import JJGKItem
from fund.sql import Sql
from bs4 import BeautifulSoup
from datetime import date


class JJGK(scrapy.Spider):

    def __init__(self):
        self.Sql = Sql()
        self.db_conn = self.Sql.conn_db('fund')

    name = "jjgk"
    custom_settings = {
        'ITEM_PIPELINES': {'fund.jjgk_pipelines.JJGKPipeline': 300},
    }

    def start_requests(self):
        sql = 'select code from fund where code not in(select code from jjgk)'
        codes = self.Sql.exec_sql(self.db_conn, sql).fetchall()
        for code in codes:
            code = code[0]
            url = 'http://fundf10.eastmoney.com/jbgk_{}.html'.format(code)
            yield scrapy.Request(url=url, callback=self.parse,  meta={'code':code})

    def parse(self, response):
        html = response.text
        code = response.meta['code']
        item = JJGKItem()

        soup = BeautifulSoup(html, 'lxml')
        boxes = soup.find('div', 'detail').find('div', 'txt_cont').find('div', 'txt_in').find_all('div', 'box')
        tds = boxes[0].find('table', 'info w790').find_all('td')
        fullname = tds[0].get_text()
        shortname = tds[1].get_text()
        type = tds[3].get_text()
        releasetime = tds[4].get_text()
        establishtime = tds[5].get_text().split('/')[0]
        establishcount = tds[5].get_text().split('/')[1]
        money = tds[6].get_text()
        count = tds[7].get_text()
        company = tds[8].get_text()
        companycode = tds[8].find('a')['href']
        bank = tds[9].get_text()
        bankcode = tds[9].find('a')['href']
        manager = tds[10].get_text()
        managercode = tds[10].find('a')
        if managercode:
            managercode = managercode['href']
        red = tds[11].get_text()
        managerfee = tds[12].get_text()
        bankfee = tds[13].get_text()
        servicefee = tds[14].get_text()
        applybuyfee = tds[15].get_text()
        buyfee = tds[16].get_text()
        salefee = tds[17].get_text()

        comparestandard = tds[18].get_text()
        tacking = tds[19].get_text()

        if len(boxes) == 8:
            del (boxes[1])
        target = boxes[1].find('p').get_text().strip('\n\r ')
        idea = boxes[2].find('p').get_text().strip('\n\r ')
        range = boxes[2].find('p').get_text().strip('\n\r ')
        strangy = boxes[2].find('p').get_text().strip('\n\r ')
        redpolicy = boxes[2].find('p').get_text().strip('\n\r ')
        risk = boxes[2].find('p').get_text().strip('\n\r ')

        leastbuy = soup.find('div', 'bs_jz').find('div', 'col-left').find('div').find('a').find_all('span')[
            -1].get_text()
        crawldate = str(date.today())


        item['code'] = code
        item['fullname'] = fullname
        item['shortname'] = shortname
        item['type'] = type
        item['releasetime'] = releasetime
        item['establishtime'] = establishtime
        item['establishcount'] = establishcount
        item['money'] = money
        item['count'] = count
        item['company'] = company
        item['companycode'] = companycode
        item['bank'] = bank
        item['bankcode'] = bankcode
        item['manager'] = manager
        item['managercode'] = managercode
        item['red'] = red
        item['managerfee'] = managerfee
        item['bankfee'] = bankfee
        item['servicefee'] = servicefee
        item['applybuyfee'] = applybuyfee
        item['buyfee'] = buyfee
        item['salefee'] = salefee
        item['comparestandard'] = comparestandard
        item['tacking'] = tacking

        item['target'] = target
        item['idea'] = idea
        item['range'] = range
        item['strangy'] = strangy
        item['redpolicy'] = redpolicy
        item['risk'] = risk
        item['leastbuy'] = leastbuy
        item['crawldate'] = crawldate


        yield item


