
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql


class JZHistoryPipeline:

    def __init__(self):
        self.conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='fund', charset='utf8')

    def exec_sql(self, sql):
        cur = self.conn.cursor()
        cur.execute(sql)
        self.conn.commit()
        cur.close()

    def process_item(self, item, spider):
        fundCode = item['fundCode']
        FSRQ = item['FSRQ']
        DWJZ = item['DWJZ']
        LJJZ = item['LJJZ']
        JZZZL = item['JZZZL']
        SGZT = item['SGZT']
        SHZT = item['SHZT']
        FHSP = item['FHSP']
        SDATE = item['SDATE']
        ACTUALSYI = item['ACTUALSYI']
        NAVTYPE = item['NAVTYPE']
        FHFCZ = item['FHFCZ']
        FHFCBZ = item['FHFCBZ']
        DTYPE = item['DTYPE']


        sql = 'insert into jzhistory(fundCode, FSRQ, DWJZ, LJJZ, JZZZL, SGZT, SHZT, FHSP, SDATE, ACTUALSYI, NAVTYPE, FHFCZ, FHFCBZ, DTYPE) values("{0}", "{1}", "{2}", "{3}", "{4}", "{5}", "{6}", "{7}", "{8}", "{9}", "{10}", "{11}", "{12}", "{13}")'.format(fundCode, FSRQ, DWJZ, LJJZ, JZZZL, SGZT, SHZT, FHSP, SDATE, ACTUALSYI, NAVTYPE, FHFCZ, FHFCBZ, DTYPE)
        self.exec_sql(sql)
        return item


