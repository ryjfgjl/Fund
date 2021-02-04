
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from fund.sql import Sql


class JJGKPipeline:

    def __init__(self):
        self.Sql = Sql()
        self.db_conn = self.Sql.conn_db('fund')

    def process_item(self, item, spider):
        code = item['code']
        fullname = item['fullname']
        shortname = item['shortname']
        type = item['type']
        releasetime = item['releasetime']
        establishtime = item['establishtime']
        establishcount = item['establishcount']
        money = item['money']
        count = item['count']
        company = item['company']
        companycode = item['companycode']
        bank = item['bank']
        bankcode = item['bankcode']
        manager = item['manager']
        managercode = item['managercode']
        red = item['red']
        managerfee = item['managerfee']
        bankfee = item['bankfee']
        servicefee = item['servicefee']
        applybuyfee = item['applybuyfee']
        buyfee = item['buyfee']
        salefee = item['salefee']
        comparestandard = item['comparestandard']
        tacking = item['tacking']

        target = item['target']
        idea = item['idea']
        range = item['range']
        strangy = item['strangy']
        redpolicy = item['redpolicy']
        risk = item['risk']
        leastbuy = item['leastbuy']
        crawldate = item['crawldate']

        sql = "insert into jjgk(code,fullname,shortname,type,releasetime,establishtime,establishcount,money,count,company,companycode," \
              "bank,bankcode,manager,managercode,red,managerfee,bankfee,servicefee,applybuyfee,buyfee,salefee,comparestandard,tacking," \
              "target,idea,`range`,strangy,redpolicy,risk,leastbuy,crawldate) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s," \
              "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        self.Sql.exec_sql(self.db_conn, sql, [
            [code, fullname, shortname, type, releasetime, establishtime, establishcount, money, count, company,
             companycode, bank, bankcode, manager, managercode, red, managerfee, bankfee, servicefee, applybuyfee,
             buyfee, salefee, comparestandard, tacking, target, idea, range, strangy, redpolicy, risk, leastbuy,
             crawldate]])

        return item


