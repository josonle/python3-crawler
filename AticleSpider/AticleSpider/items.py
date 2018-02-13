# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AticlespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title=scrapy.Field()
    author=scrapy.Field()
    country=scrapy.Field()
    publish_date=scrapy.Field()
    note=scrapy.Field()
    press=scrapy.Field()
    Score=scrapy.Field()
    Star=scrapy.Field()
    People_nums=scrapy.Field()
    s5=scrapy.Field()
    s4=scrapy.Field()
    s3=scrapy.Field()
    s2=scrapy.Field()
    s1=scrapy.Field()

    pass
