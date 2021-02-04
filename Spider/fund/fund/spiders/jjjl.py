
# http://fund.eastmoney.com/manager/30634044.html
# 基金经理
import scrapy
from fund.jjjl_items import JJJLItem, JJJLFundHistoryItem, JJJLCurrentFundItem
from fund.sql import Sql
from bs4 import BeautifulSoup
from datetime import date


class JJJL(scrapy.Spider):

    def __init__(self):
        self.Sql = Sql()
        self.db_conn = self.Sql.conn_db('fund')

    name = "jjjl"
    custom_settings = {
        'ITEM_PIPELINES': {'fund.jjjl_pipelines.JJJLPipeline': 300},
    }

    def start_requests(self):
        sql = 'select code from manager where code not in(select code from jjjl)'
        codes = self.Sql.exec_sql(self.db_conn, sql).fetchall()
        for code in codes:
            code = code[0]
            url = 'http://fund.eastmoney.com/manager/{}.html'.format(code)
            yield scrapy.Request(url=url, callback=self.parse,  meta={'code':code})

    def parse(self, response):
        html = response.text
        code = response.meta['code']
        item = JJJLItem()

        soup = BeautifulSoup(html, 'lxml')

        name = soup.find('div', 'content_out').find('div', 'content_in').find('span').get_text()
        info = soup.find('div', 'content_out').find('div', 'jlinfo clearfix').find('p').get_text()
        totalday = soup.find('div', 'content_out').find('div', 'left clearfix w438').find('div', 'right jd').get_text()
        startdate = ''
        currentcompany = soup.find('div', 'content_out').find('div', 'left clearfix w438').find('div', 'right jd').find('a').get_text()
        currentfundmoney = soup.find('div', 'content_out').find('div', 'left clearfix w438').find('div', 'right jd').\
            find('div', 'gmContainer').find('div', 'gmleft gmlefts').find('span', 'numtext').get_text()
        bestincomerate = soup.find('div', 'content_out').find('div', 'left clearfix w438').find('div', 'right jd').\
            find('div', 'gmContainer').find('div', 'gmleft').find('span', 'numtext').get_text()

        item['code'] = code
        item['name'] = name
        item['info'] = info
        item['totalday'] = totalday
        item['startdate'] = startdate
        item['currentcompany'] = currentcompany
        item['currentfundmoney'] = currentfundmoney
        item['bestincomerate'] = bestincomerate
        item['crawldate'] = str(date.today())

        yield item

        item = JJJLFundHistoryItem()
        trs = soup.find('div', 'content_out').find('table', 'ftrs').find('tbody').find_all('tr')
        for tr in trs:
            tds = tr.find_all('td')
            fundcode = tds[0].get_text()
            fundname = tds[1].get_text()
            fundtype = tds[3].get_text()
            fundmoney = tds[4].get_text()
            fundmanagerdate = tds[5].get_text()
            fundmanagerday = tds[6].get_text()
            fundmanagerincomerate = tds[7].get_text()

            item['code'] = code
            item['fundcode'] = fundcode
            item['fundname'] = fundname
            item['fundtype'] = fundtype
            item['fundmoney'] = fundmoney
            item['fundmanagerdate'] = fundmanagerdate
            item['fundmanagerday'] = fundmanagerday
            item['fundmanagerincomerate'] = fundmanagerincomerate
            item['crawldate'] = str(date.today())

            yield item

        item = JJJLCurrentFundItem()
        trs = soup.find_all('div', 'content_in')[1].find('table', 'ftrs').find('tbody').find_all('tr')
        for tr in trs:
            tds = tr.find_all('td')
            fundcode = tds[0].get_text()
            fundname = tds[1].get_text()
            fundtype = tds[2].get_text()
            last3mrate = tds[3].get_text()
            last3mrank = tds[4].get_text()
            last6mrate = tds[5].get_text()
            last6mrank = tds[6].get_text()
            last1yrate = tds[7].get_text()
            last1yrank = tds[8].get_text()
            last2yrate = tds[9].get_text()
            last2yrank = tds[10].get_text()
            currentyearrate = tds[11].get_text()
            currentyearrank = tds[12].get_text()

            item['code'] = code
            item['fundcode'] = fundcode
            item['fundname'] = fundname
            item['fundtype'] = fundtype
            item['last3mrate'] = last3mrate
            item['last3mrank'] = last3mrank
            item['last6mrate'] = last6mrate
            item['last6mrank'] = last6mrank
            item['last1yrate'] = last1yrate
            item['last1yrank'] = last1yrank
            item['last2yrate'] = last2yrate
            item['last2yrank'] = last2yrank
            item['currentyearrate'] = currentyearrate
            item['currentyearrank'] = currentyearrank
            item['crawldate'] = str(date.today())


            yield item




