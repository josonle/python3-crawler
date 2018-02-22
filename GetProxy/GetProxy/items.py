# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GetproxyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class ProxyItem(scrapy.Item):
    # ip=scrapy.Field()
    # port=scrapy.Field()
    # type=scrapy.Field()
    url=scrapy.Field()