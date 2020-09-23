# get all fund id (开放式基金)

import re
from sql import Sql
import time

class Fund:

    def __init__(self):
        self.Sql = Sql()
        self.db_conn = self.Sql.conn_db(db='fund')
    
    def main(self, driver):
        total_page = driver.find_element_by_class_name('nv').text
        total_page = int(re.search('\d+', total_page).group())
        print('total page:', total_page)
        sql = 'select crawledPage from crawl_info where spiderName = "fund"'
        crawledPage = int(self.Sql.exec_sql(self.db_conn, sql).fetchall()[0][0])
        current_page = crawledPage
        if current_page == total_page:
            return
        for i in range(total_page):
            if i < current_page:
                next_page = driver.find_elements_by_xpath("//div[@id='pager']/span[@class='nu page']")[-1]
                next_page.click()
                time.sleep(10)
                continue 
            try:
                fund_ids = driver.find_elements_by_class_name('bzdm')
                for fund_id in fund_ids:
                    fund_id = fund_id.text
                    sql = 'insert into fund(fund) select "{0}" from dual where "{0}" not in(select fund from fund)'.format(fund_id)
                    self.Sql.exec_sql(self.db_conn, sql)
                current_page += 1
                print('Crawled Page {}'.format(current_page))
                sql = 'update crawl_info set crawledPage = {} where spiderName = "fund"'.format(current_page)
                self.Sql.exec_sql(self.db_conn, sql)
                next_page = driver.find_elements_by_xpath("//div[@id='pager']/span[@class='nu page']")[-1]
                next_page.click()
                time.sleep(10)
            except Exception as reason:
                print('Spider Crawl Failed in Page {0}, {1}'.format(current_page, str(reason)))

