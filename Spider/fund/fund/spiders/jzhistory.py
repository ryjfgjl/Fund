
# http://api.fund.eastmoney.com/f10/lsjz?callback=jQuery18308439180135970412_1599727670341&fundCode=000088&pageIndex=1&pageSize=20000&startDate=&endDate=&_=1599727670359

import scrapy
import json
from fund.jzhistory_items import JZHistoryItem
import pymysql


class JZHistory(scrapy.Spider):

    def __init__(self):
        self.conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='fund', charset='utf8')

    name = "jzhistory"
    custom_settings = {
        'ITEM_PIPELINES': {'fund.jzhistory_pipelines.JZHistoryPipeline': 300},
    }

    def start_requests(self):
        sql = 'select code from fund'
        codes = self.exec_sql(sql)
        urls = []
        headers = {
            'Referer': 'http://fundf10.eastmoney.com/jjjz_000011.html',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
        }
        for code in codes:
            code = code[0]
            url = 'http://api.fund.eastmoney.com/f10/lsjz?callback=jQuery18308439180135970412_1599727670341&fundCode={0}&pageIndex=1&pageSize=20000&startDate=&endDate=&_=1599727670359'.format(code)
            yield scrapy.Request(url=url, callback=self.parse, headers=headers, meta={'code':code})

    def parse(self, response):
        html = response.text
        data = html[len('jQuery18308439180135970412_1599727670341('):-1]
        data = json.loads(data)['Data']['LSJZList']
        code = response.meta['code']

        item = JZHistoryItem()
        for d in data:
            FSRQ = d['FSRQ']
            DWJZ = d['DWJZ']
            LJJZ = d['LJJZ']
            JZZZL = d['JZZZL']
            SGZT = d['SGZT']
            SHZT = d['SHZT']
            FHSP = d['FHSP']
            SDATE = d['SDATE']
            ACTUALSYI = d['ACTUALSYI']
            NAVTYPE = d['NAVTYPE']
            FHFCZ = d['FHFCZ']
            FHFCBZ = d['FHFCBZ']
            DTYPE = d['DTYPE']

            item['fundCode'] = code
            item['FSRQ'] = FSRQ
            item['DWJZ'] = DWJZ
            item['LJJZ'] = LJJZ
            item['JZZZL'] = JZZZL
            item['SGZT'] = SGZT
            item['SHZT'] = SHZT
            item['FHSP'] = FHSP
            item['SDATE'] = SDATE
            item['ACTUALSYI'] = ACTUALSYI
            item['NAVTYPE'] = NAVTYPE
            item['FHFCZ'] = FHFCZ
            item['FHFCBZ'] = FHFCBZ
            item['DTYPE'] = DTYPE
            

            yield item


    def exec_sql(self, sql):
        cur = self.conn.cursor()
        cur.execute(sql)
        self.conn.commit()
        cur.close()
        return cur
