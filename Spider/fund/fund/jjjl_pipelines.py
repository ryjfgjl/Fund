
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from fund.sql import Sql
from fund.jjjl_items import JJJLItem, JJJLFundHistoryItem, JJJLCurrentFundItem

class JJJLPipeline:

    def __init__(self):
        self.Sql = Sql()
        self.db_conn = self.Sql.conn_db('fund')

    def process_item(self, item, spider):

        if isinstance(item, JJJLItem):
            code = item['code']
            name = item['name']
            info = item['info']
            totalday = item['totalday']
            startdate = item['startdate']
            currentcompany = item['currentcompany']
            currentfundmoney = item['currentfundmoney']
            bestincomerate = item['bestincomerate']
            crawldate = item['crawldate']

            sql = "insert into jjjl(code,name,info,totalday,startdate,currentcompany,currentfundmoney,bestincomerate,crawldate) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            self.Sql.exec_sql(self.db_conn, sql, [[code,name,info,totalday,startdate,currentcompany,currentfundmoney,bestincomerate,crawldate]])

        elif isinstance(item, JJJLFundHistoryItem):
            code = item['code']
            fundcode = item['fundcode']
            fundname = item['fundname']
            fundtype = item['fundtype']
            fundmoney = item['fundmoney']
            fundmanagerdate = item['fundmanagerdate']
            fundmanagerday = item['fundmanagerday']
            fundmanagerincomerate = item['fundmanagerincomerate']
            crawldate = item['crawldate']


            sql = "insert into jjjl_fund_history(code,fundcode,fundname,fundtype,fundmoney,fundmanagerdate,fundmanagerday,fundmanagerincomerate,crawldate) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            self.Sql.exec_sql(self.db_conn, sql, [
                [code, fundcode, fundname, fundtype, fundmoney, fundmanagerdate, fundmanagerday, fundmanagerincomerate,
                 crawldate]])
        elif isinstance(item, JJJLCurrentFundItem):
            code = item['code']
            fundcode = item['fundcode']
            fundname = item['fundname']
            fundtype = item['fundtype']
            last3mrate = item['last3mrate']
            last3mrank = item['last3mrank']
            last6mrate = item['last6mrate']
            last6mrank = item['last6mrank']
            last1yrate = item['last1yrate']
            last1yrank = item['last1yrank']
            last2yrate = item['last2yrate']
            last2yrank = item['last2yrank']
            currentyearrate = item['currentyearrate']
            currentyearrank = item['currentyearrank']
            crawldate = item['crawldate']

            sql = "insert into jjjl_current_fund(code,fundcode,fundname,fundtype,last3mrate,last3mrank,last6mrate,last6mrank,last1yrate,last1yrank,last2yrate,last2yrank,currentyearrate,currentyearrank,crawldate) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s," \
                  "%s,%s,%s)"
            self.Sql.exec_sql(self.db_conn, sql, [
                [code, fundcode, fundname, fundtype, last3mrate, last3mrank, last6mrate, last6mrank, last1yrate,
                 last1yrank, last2yrate, last2yrank, currentyearrate, currentyearrank, crawldate]])

        return item

