# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaershouItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    xiaoqu=scrapy.Field()#小区
    houseType=scrapy.Field()#三室两厅
    hasSubway=scrapy.Field()#有地铁
    houseYear=scrapy.Field()#建成时间
    totalprice=scrapy.Field()#总价
    unitprice=scrapy.Field()#单价
    meters=scrapy.Field()#面积
    location=scrapy.Field()#位置
    floor=scrapy.Field()#楼层

