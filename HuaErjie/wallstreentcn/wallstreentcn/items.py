# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WallstreentcnItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name=scrapy.Field()
    content=scrapy.Field()
    channel=scrapy.Field()
    time=scrapy.Field()
    id=scrapy.Field()
    pass

class HuaerjienewsItem(scrapy.Item):
    author=scrapy.Field()
    a_url=scrapy.Field()
    title=scrapy.Field()
    url=scrapy.Field()
    date_time=scrapy.Field()
    content_short=scrapy.Field()
    categories=scrapy.Field()
    views=scrapy.Field()

class ProxyItem(scrapy.Item):
    ip=scrapy.Field()
    port=scrapy.Field()
    type=scrapy.Field()
    location=scrapy.Field()