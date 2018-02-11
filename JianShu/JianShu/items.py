# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JianshuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name=scrapy.Field()
    id=scrapy.Field()
    following=scrapy.Field()
    follower=scrapy.Field()
    likes=scrapy.Field()
    articles=scrapy.Field()
    words=scrapy.Field()
    introduction=scrapy.Field()


    pass
