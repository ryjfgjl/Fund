
# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JJGKItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    code = scrapy.Field()
    fullname = scrapy.Field()
    shortname = scrapy.Field()
    type = scrapy.Field()
    releasetime = scrapy.Field()
    establishtime = scrapy.Field()
    establishcount = scrapy.Field()
    money = scrapy.Field()
    count = scrapy.Field()
    company = scrapy.Field()
    companycode = scrapy.Field()
    bank = scrapy.Field()
    bankcode = scrapy.Field()
    manager = scrapy.Field()
    managercode = scrapy.Field()
    red = scrapy.Field()
    managerfee = scrapy.Field()
    bankfee = scrapy.Field()
    servicefee = scrapy.Field()
    applybuyfee = scrapy.Field()
    buyfee = scrapy.Field()
    salefee = scrapy.Field()
    comparestandard = scrapy.Field()
    tacking = scrapy.Field()

    target = scrapy.Field()
    idea = scrapy.Field()
    range = scrapy.Field()
    strangy = scrapy.Field()
    redpolicy = scrapy.Field()
    risk = scrapy.Field()
    leastbuy = scrapy.Field()
    crawldate = scrapy.Field()

