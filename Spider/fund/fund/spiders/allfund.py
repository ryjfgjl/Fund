
# allfund.py
# http://fund.eastmoney.com/allfund.html

import scrapy
from bs4 import BeautifulSoup
from fund.items import FundItem


class AllFund(scrapy.Spider):
    name = "allfund"
    custom_settings = {
        'ITEM_PIPELINES': {'fund.pipelines.FundPipeline': 300},
    }

    def start_requests(self):
        urls = [
            'http://fund.eastmoney.com/allfund.html',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64…) Gecko/20100101 Firefox/68.0'})
            

    def parse(self, response):
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        num_boxes = soup.find('div', id="code_content").find_all('div', 'num_box')
        
        item = FundItem()
        for num_box in num_boxes:
            lies = num_box.find('ul').find_all('li')
            for li in lies:
                div = li.find('div')
                if not div:
                    continue
                a = div.find('a')
                if not a:
                    continue
                fund = a.string
                fund = fund.split('）')
                code = fund[0].strip('（')
                name = '）'.join(fund[1:]).strip()

                item['code'] = code
                item['name'] = name
                
                yield item


