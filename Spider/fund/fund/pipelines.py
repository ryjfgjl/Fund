# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

class FundPipeline:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='fund', charset='utf8')

    def exec_sql(self, sql):
        cur = self.conn.cursor()
        cur.execute(sql)
        self.conn.commit()
        cur.close()

    def process_item(self, item, spider):
        code = item['code']
        name = item['name']
        sql = 'insert into fund(code, name) values("{0}", "{1}")'.format(code, name)
        self.exec_sql(sql)
        return item
