# -*- coding: utf-8 -*-
import scrapy
import json,time
from wallstreentcn.items import HuaerjienewsItem


class HejnewsSpider(scrapy.Spider):
    name = 'hejnews'
    allowed_domains = ['wallstreetcn.com/news']
    start_urls = ['https://api-prod.wallstreetcn.com/apiv1/content/articles?category={}&limit=20&platform=wscn-platform'.format(p)
                  for p in['global','shares','commodities','china','us','europe','japan','charts','economy'
]]

    def parse(self, response):
        item=HuaerjienewsItem()
        # print(response.url)
        datas=json.loads(response.body)['data']['items']
        for data in datas:
            item['author']=data['author']['display_name'] if not data.get('source_name','') else data['source_name']
            item['a_url']=data['author']['uri']#作者主页
            item['title']=data['title']
            item['url']=data['uri']
            item['views']=data['pageviews']#浏览数
            item['content_short']=data['content_short']#短文
            item['categories']=data['categories']#类别
            item['date_time']=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(data['display_time']))
            yield item
        pass