# -*- coding: utf-8 -*-
import scrapy
import re
from wallstreentcn.items import ProxyItem

class ProxyspiderSpider(scrapy.Spider):
    name = 'proxySpider'
    allowed_domains = ['www.swei360.com']
    url='http://www.swei360.com/free/?page='
    start_urls = []
    for i in range(1,2):
        start_urls.append(url+str(i))

    def parse(self, response):
        item=ProxyItem()
        selector = response.xpath('//tbody//tr')
        for s in selector:
            item['ip']=s.xpath('./td[1]/text()').extract()[0]
            item['port']=s.xpath('./td[2]/text()').extract()[0]
            item['type']=s.xpath('./td[4]/text()').extract()[0]
            item['location']=s.xpath('./td[5]/text()').extract()[0]
            yield item
        pass