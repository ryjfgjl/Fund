
# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JZHistoryItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    fundCode = scrapy.Field()
    FSRQ = scrapy.Field()
    DWJZ = scrapy.Field()
    LJJZ = scrapy.Field()
    SDATE = scrapy.Field()
    ACTUALSYI = scrapy.Field()
    NAVTYPE = scrapy.Field()
    JZZZL = scrapy.Field()
    SGZT = scrapy.Field()
    SHZT = scrapy.Field()
    FHFCZ = scrapy.Field()
    FHFCBZ = scrapy.Field()
    DTYPE = scrapy.Field()
    FHSP = scrapy.Field()

