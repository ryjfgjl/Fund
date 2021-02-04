
# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JJJLItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    code = scrapy.Field()
    name = scrapy.Field()
    info = scrapy.Field()
    totalday = scrapy.Field()
    startdate = scrapy.Field()
    currentcompany = scrapy.Field()
    currentfundmoney = scrapy.Field()
    bestincomerate = scrapy.Field()
    crawldate = scrapy.Field()


class JJJLFundHistoryItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    code = scrapy.Field()
    fundcode = scrapy.Field()
    fundname = scrapy.Field()
    fundtype = scrapy.Field()
    fundmoney = scrapy.Field()
    fundmanagerdate = scrapy.Field()
    fundmanagerday = scrapy.Field()
    fundmanagerincomerate = scrapy.Field()
    crawldate = scrapy.Field()


class JJJLCurrentFundItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    code = scrapy.Field()
    fundcode = scrapy.Field()
    fundname = scrapy.Field()
    fundtype = scrapy.Field()
    last3mrate = scrapy.Field()
    last3mrank = scrapy.Field()
    last6mrate = scrapy.Field()
    last6mrank = scrapy.Field()
    last1yrate = scrapy.Field()
    last1yrank = scrapy.Field()
    last2yrate = scrapy.Field()
    last2yrank = scrapy.Field()
    currentyearrate = scrapy.Field()
    currentyearrank = scrapy.Field()
    crawldate = scrapy.Field()



