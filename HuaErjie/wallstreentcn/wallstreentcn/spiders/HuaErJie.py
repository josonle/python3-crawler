# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import re
import json,time
from wallstreentcn.items import WallstreentcnItem

class HuaerjieSpider(scrapy.Spider):
    """
    爬取
    """
    name = 'HuaErJie'
    # allowed_domains = ['wallstreetcn.com/live/global']
    # start_urls = [#最新（包含后者），股市,商品，中国，美国，欧洲，日本，数据,经济
    #               'https://api-prod.wallstreetcn.com/apiv1/content/articles?category=%s&limit=20&platform=wscn-platform'% p for p in['global','shares','commodities','china','us','europe','japan','charts','economy',]
    #               ]
    start_urls=['https://api-prod.wallstreetcn.com/apiv1/content/lives/pc?limit=10']
    list=['global','blockchain','a_stock','us_stock','forex ','commodity']

    def parse(self, response):
        news=json.loads(response.body)['data']
        item=WallstreentcnItem()
        for i in news:
            if i in self.list:
                datas=news[i]['items']
                for data in datas:
                    item['channel']=data['channels']
                    item['content']=data['content_text']
                    date_time=data['display_time']
                    item['time']=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(date_time))
                    item['id']=data['id']
                    item['name']=data['global_channel_name']
                    yield item
        pass
