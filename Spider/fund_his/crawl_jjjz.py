# 获取基金净值

import time
from sql import Sql
from driver import Driver

class JJJZ:

    def __init__(self):
        self.Sql = Sql()
        self.Driver = Driver()
        self.db_conn = self.Sql.conn_db(db='fund')

    def main(self):
        driver = self.Driver.main()
        root = 'http://fundf10.eastmoney.com/jjjz_'
        sql = 'select id,fund from fund where id > (select ifnull(crawledFundId,0) from crawl_info where spiderName = "jjjz")'
        fund_id_li = self.Sql.exec_sql(self.db_conn, sql)
        driver.implicitly_wait(2)
        for fund in fund_id_li:
            id = fund[0]
            fund = fund[1]
            jjjz_page = 0
            url = root + fund + '.html'
            driver.get(url)
            jjjz_total_page = driver.find_elements_by_xpath('//div[@class="pagebtns"]/label')[-2].text
            #sql = 'select crawledPage from crawl_info where spiderName = “jjjz”'
            #jjjz_page = int(self.Sql.exec(self.db_conn, sql))
            data = [] 
            for i in range(int(jjjz_total_page)):
            
                trs = driver.find_elements_by_xpath('//div[@id="jztable"]/table/tbody/tr') 
                for i in range(len(trs)):
                    date = driver.find_element_by_xpath('//div[@id="jztable"]/table/tbody/tr[{0}]/td[1]'.format(i+1)).text.strip()
                    unit_jz = driver.find_element_by_xpath('//div[@id="jztable"]/table/tbody/tr[{0}]/td[2]'.format(i+1)).text.strip()
                    total_jz = driver.find_element_by_xpath('//div[@id="jztable"]/table/tbody/tr[{0}]/td[3]'.format(i+1)).text.strip()
                    date_rate = driver.find_element_by_xpath('//div[@id="jztable"]/table/tbody/tr[{0}]/td[4]'.format(i+1)).text.strip()
                    buy_status = driver.find_element_by_xpath('//div[@id="jztable"]/table/tbody/tr[{0}]/td[5]'.format(i+1)).text.strip()
                    sale_status = driver.find_element_by_xpath('//div[@id="jztable"]/table/tbody/tr[{0}]/td[6]'.format(i+1)).text.strip()
                    red = driver.find_element_by_xpath('//div[@id="jztable"]/table/tbody/tr[{0}]/td[7]'.format(i+1)).text.strip()
                    data.append([id,date,unit_jz,total_jz,date_rate,buy_status,sale_status,red])
                print('Crawling Fund {0}, Crawled Page {1}'.format(fund, jjjz_page))
                jjjz_page += 1
                jjjz_next_page = driver.find_elements_by_xpath('//div[@class="pagebtns"]/label')[-1]
                jjjz_next_page.click()
                time.sleep(1)
                
            sql = "insert into jjjz(fundId,JZDate,unitJZ,totalJZ,dateRate,buyStatus,saleStatus,red) values (%s,%s,%s,%s,%s,%s,%s,%s)"
            self.Sql.exec_sql(self.db_conn,sql,data)
            sql = 'update crawl_info set crawledFundId = {} where spiderName = "jjjz"'.format(id)
            self.Sql.exec_sql(self.db_conn, sql)
                
JJJZ = JJJZ()
JJJZ,mian()









